import datetime
import re
import random

from django.contrib import auth 
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Template, Context, RequestContext, loader
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.baseconv import base36
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .forms import Login, Owner_Register, Kennel_Register, PetForm, UserForm, Forgot_Password, Reset_Password, Owner_Info_Form, Manager_Info_Form, ContactForm, NewsletterForm
from .models import Pet, Owner, Kennel, Contact, Newsletter, Blog, IndexPhoto   
from .helpers import short_salt, signup_email, forgot_password_email, account_cancelled_email, contact_email
from .groups import add_owner_perm, add_kennel_perm


class ActionMixin(object):
 
	@property 
	def action(self):
		msg = "{0} is missing action.".format(self.__class__)
		raise NotImplementedError(msg)

	def form_valid(self, form):
		msg = "{0}".format(self.action)
		messages.info(self.request, msg)
		return super(ActionMixin, self).form_valid(form)


class IndexView(FormView):

	template_name = 'pet/index.html'
	form_class = NewsletterForm
	success_url = reverse_lazy('pet:index')

	def form_valid(self, form):
		cd = form.cleaned_data
		check = Newsletter.objects.filter(email=cd['email']).exists()
		if check:
			msg = 'Your email has already been added to the Newsletter.'
			messages.info(self.request, msg)
		else:
			email = Newsletter.objects.create(email=cd['email'])
			msg = 'You have been added to our monthly newsletter.'
			messages.info(self.request, msg)
		return super(IndexView, self).form_valid(form)	

	def form_invalid(self, form):
		response = super(IndexView, self).form_invalid(form)
		msg = 'Enter a valid email address.'
		messages.info(self.request, msg)
		return response

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['blogs'] = Blog.objects.all()[:3]
		try:
			context['photo1'] = IndexPhoto.objects.order_by('-modified')[0]
			context['photo2'] = IndexPhoto.objects.order_by('-modified')[1]
			context['photo3'] = IndexPhoto.objects.order_by('-modified')[2]
		except:
			pass 
		return context


def login(request):
	if request.method == 'POST':
		form = Login(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			# form.is_active_check()
			# messages.info(request, msg)
			user = auth.authenticate(username=cd['username'], password=cd['password'])
			if user is not None and user.is_active:
				auth.login(request, user)
				messages.info(request, 'You are logged in.')
				return HttpResponseRedirect(reverse('pet:index'))
			if user is None:
				no_match = 'Please check username and password'
				return render(request, 'pet/login.html', {'form': form, 'no_match': no_match})
			if user.is_active == False:
				no_match = "Your account hasn't been activated. Please check your email in order to activate your account."
				return render(request, 'pet/login.html', {'form': form, 'no_match': no_match})
	else:
		form = Login()
	return render(request, 'pet/login.html', {'form': form})


class ManagerListView(ListView):

	model = Kennel

	def get_queryset(self):
		queryset = super(ManagerListView, self).get_queryset()
		q = self.request.GET.get('q')
		if q:
			return queryset.filter(kennel_name__icontains=q)[:5]
		else:
			queryset = None
		return queryset


@login_required(login_url='/accounts/login/')
def owner_view_of_manager(request, pk, salt):
	kennel = Kennel.objects.get(pk=pk, salt=salt)
	owner = Owner.objects.get(owner=request.user)
	try:
		connected_owner = Kennel.objects.get(owners=owner, pk=pk)
	except:
		connected_owner = None  
	if connected_owner is not None: 
		return render(request, 'pet/owner_view_of_manager.html', {'kennel': kennel, 'connected_owner': connected_owner})
	else:
		return render(request, 'pet/owner_view_of_manager.html', {'kennel': kennel})


@login_required(login_url='/accounts/login/')
def add_kennel_connection(request, pk, salt):
	manager = Kennel.objects.get(pk=pk, salt=salt)
	owner = Owner.objects.get(owner=request.user)
	if request.method == 'POST':
		manager.owners.add(owner)
		manager.save()
		msg = "{0} has been added to your list of kennel connections".format(manager.kennel_name)
		messages.info(request, msg)
		return HttpResponseRedirect(reverse('pet:redirect_to_account', kwargs={'pk':request.user.pk}))
	else:
		pass
	return render(request, 'pet/add_kennel_connection.html', {'manager':manager})


@login_required(login_url='/accounts/login/')
def remove_kennel_connection(request, pk, salt):
	manager = Kennel.objects.get(pk=pk, salt=salt)
	owner = Owner.objects.get(owner=request.user)
	if request.method == 'POST':
		manager.owners.remove(owner)
		manager.save()
		msg = "{0} has been removed to your list of kennel connections".format(manager.kennel_name)
		messages.info(request, msg)
		return HttpResponseRedirect(reverse('pet:redirect_to_account', kwargs={'pk':request.user.pk}))
	else:
		pass
	return render(request, 'pet/remove_kennel_connection.html', {'manager':manager})


@login_required(login_url=reverse_lazy('pet:login'))
def logout(request):
	auth.logout(request)
	messages.info(request, 'You are now logged out')
	return HttpResponseRedirect(reverse('pet:index'))


class PetCheckMixin(object):

	def get_object(self):
		pet = get_object_or_404(Pet, pk=self.kwargs['pk'])
		my_owner = get_object_or_404(Owner, owner=self.request.user)
		my_pets= my_owner.pets.all()

		can_view = False
		for i in range(len(my_pets)):
			if my_pets[i].pk == int(pet.pk):
				can_view = True

		if can_view != True:
			raise Http404

		return pet


class OwnerCheckMixin(object):

	def get_object(self):
		owner = get_object_or_404(Owner, pk=self.kwargs['pk'])

		if owner.owner != self.request.user:
			raise Http404

		return owner


class KennelCheckMixin(object):

	def get_object(self):
		kennel = get_object_or_404(Kennel, pk=self.kwargs['pk'])

		if kennel.manager != self.request.user:
			raise Http404

		return kennel


class PetCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

	model = Pet 
	template_name = 'pet/basic_form.html'
	form_class = PetForm
	permission_required = 'pet.is_a_owner'

	def get_context_data(self, **kwargs):
		context = super(PetCreateView, self).get_context_data(**kwargs)
		context['form_title'] = ' Add my Pet'
		return context

	def get_success_url(self):
		pet = self.model.objects.get(pk=self.object.pk)
		owner = Owner.objects.get(owner=self.request.user)
		owner.pets.add(pet)
		owner.save()
		return reverse('pet:pet_detail', kwargs={'pk':self.object.pk, 'slug':self.object.slug})


class PetUpdateView(LoginRequiredMixin, PetCheckMixin, UpdateView):

	model = Pet
	template_name = 'pet/basic_form.html'
	form_class = PetForm

	def get_context_data(self, **kwargs):
		context = super(PetUpdateView, self).get_context_data(**kwargs)
		context['form_title'] = ' Update Pet'
		return context

	def get_success_url(self):
		return reverse_lazy('pet:pet_detail', kwargs={'pk':self.object.pk, 'slug':self.object.slug})


class PetDetailView(LoginRequiredMixin, PetCheckMixin, DetailView):

	model = Pet 


class PetDeleteView(LoginRequiredMixin, PetCheckMixin, DeleteView):

	model = Pet 
	template_name = 'pet/pet_delete_form.html'

	def get_context_data(self, **kwargs):
		context = super(PetDeleteView, self).get_context_data(**kwargs)
		pet = get_object_or_404(Pet, pk=self.kwargs['pk'])
		context['pet'] = pet 
		return context

	def get_success_url(self):
		return reverse_lazy('pet:redirect_to_account', kwargs={'pk':self.request.user.pk})


class ForgotPasswordView(FormView):

	template_name = 'pet/forgot_password.html'
	form_class = Forgot_Password
	success_url = reverse_lazy('pet:password_email_sent')

	def form_valid(self, form):
		cd = form.cleaned_data
		username = cd['username']
		email = cd['email']
		try:
			user = User.objects.get(username=cd['username'], email=cd['email'])
			messages.info(self.request, 'A reset password email has been sent. Please check your email.')
		except:
			messages.info(self.request, 'Username and email do not match.')
			return HttpResponseRedirect(reverse('pet:forgot_password'))
		if user.email == email and user is not None and user.is_active:
			temp_password = short_salt()
			user.set_password(temp_password)
			user.save()
			msg = forgot_password_email(username, email, temp_password)
			msg.send()
		return super(ForgotPasswordView, self).form_valid(form)


class ContactEmailSentView(TemplateView):

	template_name = 'pet/contact_email_sent.html'


class PasswordEmailSentView(TemplateView):

	template_name = 'pet/password_email_sent.html'


class ResetPasswordView(FormView):

	template_name = 'pet/reset_password.html'
	form_class = Reset_Password
	success_url = reverse_lazy('pet:index')

	def form_valid(self, form):
		cd = form.cleaned_data
		form.clean_username()
		user = auth.authenticate(username=cd['username'], password=cd['temp_password'])
		# user = User.objects.get(username=username)
		if user is not None and user.is_active:
			user.set_password(cd['new_password'])
			user.save()
			user = auth.authenticate(username=cd['username'], password=cd['new_password'])
			auth.login(self.request, user)
		return super(ResetPasswordView, self).form_valid(form)


class OwnerCreateAccount(FormView):

	template_name = 'pet/create_account.html'
	form_class = Owner_Register
	success_url = reverse_lazy('pet:register_success')

	def get_context_data(self, **kwargs):
		context = super(OwnerCreateAccount, self).get_context_data(**kwargs)
		context['form_title'] = ' Create Pet Owner Account'
		return context

	def form_valid(self, form):
		cd = form.cleaned_data
		form.clean_username()
		user = User.objects.create_user(**form.cleaned_data)
		if user is not None:
			# create "owner" linked to newly added user
			owner = Owner.objects.create(owner=user, name=user.username)
			user = auth.authenticate(username=cd['username'], password=cd['password'])
			add_owner_perm(user.pk)
			# mark user as inactive until they activate thro email link
			user.is_active = False
			user.save()
			# send confirmation email
			msg = signup_email(username=cd['username'], email=cd['email'], pk=user.pk, signup_link=owner.salt)
			msg.send()
		return super(OwnerCreateAccount, self).form_valid(form)


class OwnerProfileView(LoginRequiredMixin, OwnerCheckMixin, DetailView):

	model = User
	template_name = 'pet/profile.html'

	def get_context_data(self, **kwargs):
		context = super(OwnerProfileView, self).get_context_data(**kwargs)
		context['owner'] = get_object_or_404(Owner, owner=self.request.user)
		context['pets'] = Pet.objects.filter(owner=context['owner'])
		context['managers'] = Kennel.objects.filter(owners=context['owner'])
		return context


@login_required(login_url='/accounts/login/')
def remove_kennel_connection(request, pk, salt):
	manager = Kennel.objects.get(pk=pk, salt=salt)
	owner = Owner.objects.get(owner=request.user)
	if request.method == 'POST':
		manager.owners.remove(owner)
		manager.save()
		return HttpResponseRedirect(reverse('pet:redirect_to_account', kwargs={'pk':request.user.pk}))
	else:
		pass
	return render(request, 'pet/remove_kennel_connection.html', {'manager':manager})	


class ManagerCreateAccount(FormView):

	template_name = 'pet/create_account.html'
	form_class = Kennel_Register
	success_url = reverse_lazy('pet:register_success')

	def form_valid(self, form):
		cd = form.cleaned_data
		form.clean_username()
		user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
		if user is not None:
			# create "kennel" based upon newly added user
			kennel = Kennel.objects.create(manager=user, kennel_name=cd['kennel_name'])
			user = auth.authenticate(username=cd['username'], password=cd['password'])
			add_kennel_perm(user.pk)
			# mark user as inactive until they activate thro email link
			user.is_active = False
			user.save()
			# send confirmation email
			msg = signup_email(username=cd['username'], email=cd['email'], pk=user.pk, signup_link=kennel.salt)
			msg.send()
		return super(ManagerCreateAccount, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(ManagerCreateAccount, self).get_context_data(**kwargs)
		context['form_title'] = ' Create Pet Manager Account'
		return context


class OwnerUpdateView(LoginRequiredMixin, OwnerCheckMixin, UpdateView):

	model = Owner
	template_name = 'pet/basic_form.html'
	form_class = Owner_Info_Form

	def get_context_data(self, **kwargs):
		context = super(OwnerUpdateView, self).get_context_data(**kwargs)
		context['form_title'] = ' Pet Owner Update Form'
		return context

	def form_valid(self, form):
		# User Fields
		user = User.objects.get(pk=self.request.user.pk)
		user.email = form.cleaned_data['email']
		user.save()
		return super(OwnerUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('pet:redirect_to_account', kwargs={'pk':self.request.user.pk})


class ManagerUpdateView(LoginRequiredMixin, KennelCheckMixin, UpdateView):

	model = Kennel
	template_name = 'pet/basic_form.html'
	form_class = Manager_Info_Form
	action = 'Your account has been successfully updated'

	def get_context_data(self, **kwargs):
		context = super(ManagerUpdateView, self).get_context_data(**kwargs)
		context['form_title'] = ' Manager Update Form'
		return context

	def form_valid(self, form):
		# User Fields
		user = User.objects.get(pk=self.request.user.pk)
		user.email = form.cleaned_data['email']
		user.save()
		return super(ManagerUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('pet:redirect_to_account', kwargs={'pk':self.request.user.pk})


@login_required(login_url='/accounts/login/')
def redirect_to_account(request, pk):
	try:
		owner = get_object_or_404(Owner, owner=request.user)
		if owner.owner == request.user:
			return HttpResponseRedirect(reverse('pet:owner_profile', kwargs={'pk':owner.pk}))
	except:
		pass 
	try: 
		kennel = get_object_or_404(Kennel, manager=request.user)
		if kennel.manager == request.user:
			return HttpResponseRedirect(reverse('pet:manager_profile', kwargs={'pk':kennel.pk}))
	except:
		pass
	if owner and kennel is None: raise Http404
	return HttpResponseRedirect(reverse('pet:index'))


class ManagerProfileView(LoginRequiredMixin, KennelCheckMixin, DetailView):

	model = User 
	template_name = 'pet/kennel_profile.html'

	def get_context_data(self, **kwargs):
		context = super(ManagerProfileView, self).get_context_data(**kwargs)
		context['kennel'] = get_object_or_404(Kennel, manager=self.request.user)
		return context


@login_required(login_url='/accounts/login/')
def ro_owner_profile(request, pk, salt):
	owner= Owner.objects.get(pk=pk, salt=salt)
	pets = Pet.objects.filter(owner__pk=pk)
	return render(request, 'pet/profile.html', {'owner':owner, 'pets':pets})


@login_required(login_url='/accounts/login/')
def ro_pet_profile(request, pk, salt):
	pet = Pet.objects.get(pk=pk, salt=salt)
	return render(request, 'pet/pet_detail.html', {'pet':pet})



class UserDeleteView(LoginRequiredMixin, DeleteView):

	model = User
	template_name = 'pet/account_delete_form.html'
	success_url = reverse_lazy('pet:account_cancelled')

	def post(self, request, *args, **kwargs):
		user = self.request.user
		msg = account_cancelled_email(user.username, user.email)
		msg.send(fail_silently=False)
		auth.logout(request)
		user.delete()
		return HttpResponseRedirect(self.success_url)


class AccountCancelledView(TemplateView):

	template_name = 'pet/account_cancelled.html'


class RegisterSuccessView(TemplateView):

	template_name = 'pet/register_success.html'


def activate(request, pk, salt):
	user = User.objects.get(pk=pk)
	user.is_active = True
	user.save()
	return HttpResponseRedirect(reverse('pet:activate_success'))


class ActivateSuccessView(TemplateView):

	template_name = 'pet/activate_success.html'


class ContactView(FormView):

	template_name = 'pet/contact.html'
	success_url = reverse_lazy('pet:contact_email_sent')
	form_class = ContactForm

	def form_valid(self, form):
		cd = form.cleaned_data
		contact = Contact.objects.create(**form.cleaned_data)
		if contact is not None:
			# send contact email
			msg = contact_email(name=cd['name'], email=cd['email'], subject=cd['subject'], message=cd['message'])
			msg.send()
		return super(ContactView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(ContactView, self).get_context_data(**kwargs)
		context['form_title'] = ' Contact Us'
		context['button_title'] = 'Submit'
		return context


class PrivacyPolicyView(TemplateView):

	template_name = 'pet/privacy_policy.html'


class TermsAndConditionsView(TemplateView):

	template_name = 'pet/terms_and_conditions.html'

	def get_context_data(self, **kwargs):
		context = super(TermsAndConditionsView, self).get_context_data(**kwargs)
		context['company_name'] = 'Pet Stayz'
		return context


class MissionStatementView(TemplateView):

	template_name = 'pet/mission_statement.html'


class WhereToStartView(TemplateView):

	template_name = 'pet/where_to_start.html'


class SitemapView(TemplateView):

	template_name = 'pet/sitemap.html'





