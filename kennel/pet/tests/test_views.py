"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
import re 
import random

from django.test import TestCase, LiveServerTestCase
from django.test.client import Client

from django.contrib import auth 
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Template, Context, RequestContext, loader
from django.core.urlresolvers import reverse, reverse_lazy  
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User, Group, Permission 
from django.contrib.contenttypes.models import ContentType 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.baseconv import base36
from django.contrib import messages

from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from selenium.webdriver.firefox.webdriver import WebDriver

from pet.forms import Login, Owner_Register, Kennel_Register, PetForm, UserForm, Forgot_Password, Reset_Password
from pet.models import Pet, Owner, Kennel 
from pet.helpers import short_salt, signup_email, forgot_password_email, account_cancelled_email
from pet.groups import add_owner_group, add_kennel_group, add_owner_permissions, add_kennel_permissions, give_perm_to_owner_group, give_perm_to_kennel_group, add_owner_perm, add_kennel_perm
from testdata import CreateTestData


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class IndexViewTests(TestCase):

	def setUp(self):
		# Create Users
		self.evelyn = User.objects.create_user('Evelyn', 'pyaaron@gmail.com', '1234')
		self.yuki = User.objects.create_user('Yuki', 'pyaaron@gmail.com', '1234')
		self.lauren = User.objects.create_user('Lauren', 'pyaaron@gmail.com', '1234') 
		self.dad = User.objects.create_user('Dad', 'pyaaron@gmail.com', '1234')
		self.miles = User.objects.create_user('Miles', 'pyaaron@gmail.com', '1234')

		# Create Pets
		self.bobbi = Pet.objects.create(name='Bobbi', age='1', food='dry food', emergency='tropicana')
		self.dino = Pet.objects.create(name='Dino', age='1', food='dry food', emergency='tropicana')
		self.hama = Pet.objects.create(name='Hama', age='1', food='dry food', emergency='tropicana')

		# Create Kennels
		self.evelynKennel = Kennel.objects.create(kennel_name="Evelyn's Kennel", manager=self.evelyn, name=self.evelyn.username)
		self.dadKennel = Kennel.objects.create(kennel_name="Dad's Kennel", manager=self.dad, name=self.dad.username)

		# Create Owners
		self.yukiOwner = Owner.objects.create(name='Yuki', owner=self.yuki)
		self.laurenOwner = Owner.objects.create(name='Lauren', owner=self.lauren)
		self.milesOwner = Owner.objects.create(name='Miles', owner=self.miles)

		# Join Pets to Owners
		self.yukiOwner.pets = [self.bobbi.id, self.dino.id]
		self.yukiOwner.save()
		self.laurenOwner.pets.add(self.hama.id)
		self.laurenOwner.save()

		# Join Owners to Managers
		self.evelynKennel.owners.add(self.yukiOwner)
		self.evelynKennel.save()

		# Add Owner permissions to Owners
		self.owner_users = Group.objects.create(name='Owner Users')
		self.owner_ct = ContentType.objects.get(app_label='pet', model='owner')
		self.is_owner = Permission.objects.create(name='Is Owner', codename='is_a_owner', content_type=self.owner_ct)
		# add Permission to Group
		self.owner_users.permissions.add(self.is_owner)
		self.owner_users.save()
		# add User to Group
		self.yuki.groups.add(self.owner_users)
		self.yuki.save()
		self.lauren.groups.add(self.owner_users)
		self.lauren.save()

		# Add Kennel permissions to Kennel
		self.kennel_users = Group.objects.create(name='Kennel Users')
		self.kennel_ct = ContentType.objects.get(app_label='pet', model='kennel')
		self.is_kennel = Permission.objects.create(name='Is Kennel', codename='is_a_kennel', content_type=self.kennel_ct)
		# add Permission to Group
		self.kennel_users.permissions.add(self.is_kennel)
		self.kennel_users.save()
		# add User to Group
		self.evelyn.groups.add(self.kennel_users)
		self.evelyn.save()

		# Not Active user to test
		self.inactive_user = User.objects.create_user('inactive_user', 'pyaaron@gmail.com', '1234')
		self.inactive_user.is_active = False
		self.inactive_user.save()


	def test_data_created(self):
		all_users = User.objects.all()
		self.assertEqual(len(all_users), 6)


	def test_owner_profile_content_pets(self):
		self.client.login(username='Yuki', password='1234')
		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk':self.yukiOwner.pk}))
		self.assertContains(response, 'Bobbi')
		self.assertNotContains(response, 'Hama')

		self.yukiOwner.pets.add(self.hama.id)
		self.yukiOwner.save()
		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk':self.yukiOwner.pk}))
		self.assertContains(response, 'Hama')
		
		self.yukiOwner.pets.remove(self.hama.id)
		self.yukiOwner.save()
		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk':self.yukiOwner.pk}))
		self.assertNotContains(response, 'Hama')


	def test_owner_profile_content_kennels(self):
		self.client.login(username='Yuki', password='1234')
		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk':self.yukiOwner.pk}))
		self.assertContains(response, "Evelyn")
		self.assertNotContains(response, "Dad")

		self.dadKennel.owners.add(self.yukiOwner)
		self.dadKennel.save()
		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk':self.yukiOwner.pk}))
		self.assertContains(response, "Dad")

		self.dadKennel.owners.remove(self.yukiOwner)
		self.dadKennel.save()
		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk':self.yukiOwner.pk}))
		self.assertNotContains(response, "Dad")


	def test_kennel_profile_owners(self):
		self.client.login(username='Evelyn', password='1234')
		response = self.client.get(reverse('pet:manager_profile', kwargs={'pk':self.evelynKennel.pk}))
		self.assertContains(response, 'Yuki')
		self.assertNotContains(response, 'Lauren')


	def test_kennel_profile_add_owners(self):
		self.client.login(username='Evelyn', password='1234')
		self.evelynKennel.owners.add(self.laurenOwner)
		self.evelynKennel.save()
		response = self.client.get(reverse('pet:manager_profile', kwargs={'pk':self.evelynKennel.pk}))
		self.assertContains(response, 'Lauren')


	def test_kennel_profile_remove_owners(self):
		self.client.login(username='Evelyn', password='1234')
		self.evelynKennel.owners.remove(self.laurenOwner)
		self.evelynKennel.save()
		response = self.client.get(reverse('pet:manager_profile', kwargs={'pk':self.evelynKennel.pk}))
		self.assertNotContains(response, 'Lauren')


	def test_kennel_profile_owners_pets(self):
		self.client.login(username='Evelyn', password='1234')
		response = self.client.get(reverse('pet:manager_profile', kwargs={'pk':self.evelynKennel.pk}))
		self.assertContains(response, 'Bobbi')
		self.assertContains(response, 'Dino')

		self.yukiOwner.pets.add(self.hama.id)
		self.yukiOwner.save()
		response = self.client.get(reverse('pet:manager_profile', kwargs={'pk':self.evelynKennel.pk}))
		self.assertContains(response, 'Hama')
		
		self.yukiOwner.pets.remove(self.hama.id)
		self.yukiOwner.save()
		response = self.client.get(reverse('pet:manager_profile', kwargs={'pk':self.evelynKennel.pk}))
		self.assertNotContains(response, 'Hama')


	def test_ro_view_owner(self):
		self.client.login(username='Evelyn', password='1234')
		response = self.client.get(reverse('pet:ro_owner_profile', kwargs={'pk':self.yukiOwner.pk, 'salt':self.yukiOwner.salt}))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Yuki')
		self.assertNotContains(response, 'Update Profile')
		self.assertNotContains(response, 'Add a Pet')
		self.assertNotContains(response, 'My Kennel Managers')


	def test_ro_view_pet(self):
		self.client.login(username='Evelyn', password='1234')
		response = self.client.get(reverse('pet:ro_pet_profile', kwargs={'pk':self.bobbi.pk, 'salt':self.bobbi.salt}))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Bobbi')
		self.assertNotContains(response, 'Update')
		self.assertNotContains(response, 'Remove')


	def test_ro_view_owner_logged_out(self):
		response = self.client.get(reverse('pet:ro_owner_profile', kwargs={'pk':self.yukiOwner.pk, 'salt':self.yukiOwner.salt}))
		self.assertEqual(response.status_code, 302)
		self.assertNotEqual(response.status_code, 200)


	def test_ro_view_pet_logged_out(self):
		response = self.client.get(reverse('pet:ro_pet_profile', kwargs={'pk':self.bobbi.pk, 'salt':self.bobbi.salt}))
		self.assertEqual(response.status_code, 302)
		self.assertNotEqual(response.status_code, 200)


	def test_owner_view_of_manager(self):
		self.client.login(username='Yuki', password='1234')
		response = self.client.get(reverse('pet:owner_view_of_manager', kwargs={'pk':self.evelynKennel.pk, 'salt':self.evelynKennel.salt}))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Evelyn')


	def test_owner_view_of_manager_logged_out(self):
		response = self.client.get(reverse('pet:owner_view_of_manager', kwargs={'pk':self.evelynKennel.pk, 'salt':self.evelynKennel.salt}))
		self.assertNotEqual(response.status_code, 200)	
		self.assertEqual(response.status_code, 302)


	def test_add_kennel_connection_view(self):
		self.client.login(username='Yuki', password='1234')
		response = self.client.get(reverse('pet:add_kennel_connection', kwargs={'pk':self.dadKennel.pk, 'salt':self.dadKennel.salt}))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Dad')


	def test_add_kennel_connection_view_logged_out(self):
		response = self.client.get(reverse('pet:owner_view_of_manager', kwargs={'pk':self.dadKennel.pk, 'salt':self.dadKennel.salt}))
		self.assertNotEqual(response.status_code, 200)	
		self.assertEqual(response.status_code, 302)


	def test_kennel_view_pet_edits(self):
		self.client.login(username='Evelyn', password='1234')

		# this may be a failing test, where a Kennel can create a pet?
		response = self.client.get(reverse('pet:pet_create_form'))
		self.assertNotEqual(response.status_code, 200)
		self.assertEqual(response.status_code, 302)

		response = self.client.get(reverse('pet:pet_detail', kwargs={'pk': self.bobbi.pk, 'slug': self.bobbi.slug}))
		self.assertEqual(response.status_code, 404)

		response = self.client.get(reverse('pet:pet_update_form', kwargs={'pk': self.bobbi.pk, 'slug': self.bobbi.slug}))
		self.assertEqual(response.status_code, 404)

		response = self.client.get(reverse('pet:pet_delete_form', kwargs={'pk': self.bobbi.pk, 'slug': self.bobbi.slug}))
		self.assertEqual(response.status_code, 404)


	def test_another_owner_edit_dif_owners_pets(self):
		self.client.login(username='Lauren', password='1234')

		response = self.client.get(reverse('pet:pet_detail', kwargs={'pk': self.bobbi.pk, 'slug': self.bobbi.slug}))
		self.assertEqual(response.status_code, 404)

		response = self.client.get(reverse('pet:pet_update_form', kwargs={'pk': self.bobbi.pk, 'slug': self.bobbi.slug}))
		self.assertEqual(response.status_code, 404)

		response = self.client.get(reverse('pet:pet_delete_form', kwargs={'pk': self.bobbi.pk, 'slug': self.bobbi.slug}))
		self.assertEqual(response.status_code, 404)


	def test_dif_user_cant_view_other_owners_accounts(self):
		self.client.login(username='Lauren', password='1234')

		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk': self.yukiOwner.pk}))
		self.assertEqual(response.status_code, 404)

		response = self.client.get(reverse('pet:owner_update_form', kwargs={'pk': self.yukiOwner.pk}))
		self.assertEqual(response.status_code, 404)


	def test_dif_user_cant_view_other_kennels_accounts(self):

		# Login as Evelyn the Kennel and try to view Dad's Kennel pages
		self.client.login(username='Evelyn', password='1234')

		response = self.client.get(reverse('pet:manager_profile', kwargs={'pk': self.dadKennel.pk}))
		self.assertEqual(response.status_code, 404)

		response = self.client.get(reverse('pet:manager_update_form', kwargs={'pk': self.dadKennel.pk}))
		self.assertEqual(response.status_code, 404)


	def test_index_logged_in(self):
		self.client.login(username='Yuki', password='1234')
		response = self.client.get(reverse('pet:index'))
		self.assertEqual(response.status_code, 200)
		self.assertNotEqual(response.content, {})


	def test_index_with_no_user_logged_in(self):
		self.client.logout()
		response = self.client.get(reverse('pet:index'))
		self.assertEqual(response.status_code, 200)


	def test_login_view(self):
		response = self.client.get(reverse('pet:login'))
		self.assertEqual(response.status_code, 200)

		self.client.login(username='Yuki', password='1234')
		response = self.client.get(reverse('pet:login'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'You are currently logged in')


	def test_login_for_owner(self):
		response = self.client.post('/accounts/login/', {'username':'Yuki', 'password':'1234'})
		self.assertEqual(response.status_code, 302)


	def test_login_for_manager(self):
		response = self.client.post('/accounts/login/', {'username':'Evelyn', 'password':'1234'})
		self.assertEqual(response.status_code, 302)


	def test_index_view(self):
		response = self.client.get(reverse('pet:index'))
		self.assertEqual(response.status_code, 200)


	def test_redirect_to_account(self):
		response = self.client.get(reverse('pet:redirect_to_account', kwargs={'pk':1}))
		self.assertEqual(response.status_code, 302)

		self.client.login(username='Yuki', password='1234')
		response = self.client.get(reverse('pet:redirect_to_account', kwargs={'pk':self.yuki.pk}))
		self.assertEqual(response.status_code, 302)

		response = self.client.get(reverse('pet:redirect_to_account', kwargs={'pk':10}))
		self.assertEqual(response.status_code, 302)


	def test_login_with_inactive_user(self):
		self.client.login(username='inactive_user', password='1234')
		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk':self.inactive_user.pk}))
		self.assertNotEqual(response.status_code, 200)

		response = self.client.get(reverse('pet:manager_profile', kwargs={'pk':self.inactive_user.pk}))
		self.assertNotEqual(response.status_code, 200)

		response = self.client.post('/accounts/login/', {'username':'inactive_user', 'password':'1234'})
		self.assertEqual(response.status_code, 200)
		

	def test_owner_profile(self):
		self.client.login(username='Yuki', password='1234')
		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk':self.yukiOwner.pk}))
		self.assertEqual(response.status_code, 200)

		self.client.logout()
		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk':self.yuki.pk}))
		self.assertEqual(response.status_code, 302)

		self.client.login(username='Evelyn', password='1234')
		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk':self.yuki.pk}))
		self.assertNotEqual(response.status_code, 200)
		self.assertEqual(response.status_code, 404)


	def test_manager_profile(self):
		self.client.login(username='Evelyn', password='1234')
		response = self.client.get(reverse('pet:manager_profile', kwargs={'pk':self.evelynKennel.pk}))
		self.assertEqual(response.status_code, 200)

		self.client.logout()
		response = self.client.get(reverse('pet:manager_profile', kwargs={'pk':self.evelyn.pk}))
		self.assertEqual(response.status_code, 302)

		self.client.login(username='Yuki', password='1234')
		response = self.client.get(reverse('pet:manager_profile', kwargs={'pk':self.evelyn.pk}))
		self.assertNotEqual(response.status_code, 200)
		self.assertEqual(response.status_code, 404)


	def test_create_account(self):
		self.client.login(username='Yuki', password='1234')
		response = self.client.get(reverse('pet:create_account'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Logout')

		self.client.logout()
		response = self.client.get(reverse('pet:create_account'))
		self.assertEqual(response.status_code, 200)

		response = self.client.post('/owner-create/', {'username':'newuser_owner', 'email':'pyaaron@gmail.com', 'password':'1234'})
		self.assertEqual(response.status_code, 302)


	def test_manager_create_account(self):
		self.client.login(username='Evelyn', password='1234')
		response = self.client.get(reverse('pet:manager_create_account'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Logout')

		self.client.logout()
		response = self.client.get(reverse('pet:manager_create_account'))
		self.assertEqual(response.status_code, 200)

		response = self.client.post('/manager-create/', {'username':'newuser_manager_2', 'email':'pyaaron@gmail.com', 'password':'1234'})
		self.assertEqual(response.status_code, 200)


	def test_register_success(self):
		response = self.client.get(reverse('pet:register_success'))
		self.assertEqual(response.status_code, 200)


	def test_activate(self):
		response = self.client.get(reverse('pet:activate', kwargs={'pk':self.yuki.pk, 'salt':self.yukiOwner.salt}))
		self.assertEqual(response.status_code, 302)

	def test_activate_success(self):
		response = self.client.get(reverse('pet:activate_success'))
		self.assertEqual(response.status_code, 200)

	def test_logout(self):
		self.client.logout()
		response = self.client.get(reverse('pet:logout'))
		self.assertEqual(response.status_code, 302)

	def test_forgot_password(self):
		response = self.client.get(reverse('pet:forgot_password'))
		self.assertEqual(response.status_code, 200)

	def test_contact_email_sent(self):
		response = self.client.get(reverse('pet:contact_email_sent'))
		self.assertEqual(response.status_code, 200)

	def test_password_email_sent(self):
		response = self.client.get(reverse('pet:password_email_sent'))
		self.assertEqual(response.status_code, 200)

	def test_reset_password(self):
		response = self.client.get(reverse('pet:reset_password'))
		self.assertEqual(response.status_code, 200)


	def test_pet_create_view(self):
		self.client.login(username='newuser', password='1234')
		response = self.client.get(reverse('pet:pet_create_form'))
		self.assertEqual(response.status_code, 302)
		self.client.logout()
		response = self.client.get(reverse('pet:pet_create_form'))
		self.assertNotEqual(response.status_code, 404)
		self.assertEqual(response.status_code, 302)

	def test_pet_update_view(self):
		self.client.login(username='newuser', password='1234')
		pet_to_update = Pet.objects.create(name='testpet', age='1', food='eats twice daily dry food', emergency='tropicana animal hospital')
		response = self.client.get(reverse('pet:pet_update_form', kwargs={'pk': pet_to_update.pk, 'slug':pet_to_update.slug}))
		self.assertEqual(response.status_code, 302)
		self.client.logout()
		response = self.client.get(reverse('pet:pet_update_form', kwargs={'pk': pet_to_update.pk, 'slug':pet_to_update.slug}))
		self.assertEqual(response.status_code, 302)
		self.assertNotEqual(response.status_code, 404)



	def test_pet_delete_view(self):
		self.client.login(username='newuser', password='1234')
		pet_to_delete = Pet.objects.create(name='testpet', age='1', food='eats twice daily dry food', emergency='tropicana animal hospital')
		response = self.client.get(reverse('pet:pet_delete_form', kwargs={'pk': pet_to_delete.pk, 'slug':pet_to_delete.slug}))		
		self.assertEqual(response.status_code, 302)
		self.client.logout()
		response = self.client.get(reverse('pet:pet_delete_form', kwargs={'pk': pet_to_delete.pk, 'slug':pet_to_delete.slug}))
		self.assertEqual(response.status_code, 302)
		self.assertNotEqual(response.status_code, 404)


	def test_owner_views(self):
		self.user = User.objects.create_user('newuser', 'pyaaron@gmail.com', '1234')
		self.owner = Owner.objects.create(name='testowner', owner=self.user)
		self.client.login(username='newuser', password='1234')

		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk':self.owner.pk}))
		self.assertEqual(response.status_code, 200)

		response = self.client.get(reverse('pet:owner_update_form', kwargs={'pk':self.owner.pk}))
		self.assertEqual(response.status_code, 200)

		response = self.client.get(reverse('pet:activate', kwargs={'pk':self.user.pk, 'salt':self.owner.salt}))
		self.assertEqual(response.status_code, 302)


	def test_kennel_views(self):
		self.user = User.objects.create_user('newuser', 'pyaaron@gmail.com', '1234')
		self.kennel = Kennel.objects.create(kennel_name='test_kennel', manager=self.user)
		self.client.login(username='newuser', password='1234')

		response = self.client.get(reverse('pet:manager_profile', kwargs={'pk':self.kennel.pk}))
		self.assertEqual(response.status_code, 200)

		response = self.client.get(reverse('pet:manager_update_form', kwargs={'pk':self.kennel.pk}))
		self.assertEqual(response.status_code, 200)

		response = self.client.get(reverse('pet:activate', kwargs={'pk':self.user.pk, 'salt':self.kennel.salt}))
		self.assertEqual(response.status_code, 302)


	def test_contact_view(self):
		response = self.client.get(reverse('pet:contact'))
		self.assertEqual(response.status_code, 200)


	def test_owner_create_test_view(self):
		response = self.client.get(reverse('pet:create_account'))
		self.assertEqual(response.status_code, 200)

		self.client.login(username='Yuki', password='1234')
		response = self.client.get(reverse('pet:create_account'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Logout')


	def test_owner_profile_view_logged_in(self):
		self.client.login(username='Yuki', password='1234')
		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk':self.yukiOwner.pk}))
		self.assertEqual(response.status_code, 200)

		self.client.logout()

		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk':self.yukiOwner.pk}))
		self.assertNotEqual(response.status_code, 200)
		self.assertEqual(response.status_code, 302)


	def test_owner_update_view_logged_in(self):
		self.client.login(username='Yuki', password='1234')
		response = self.client.get(reverse('pet:owner_update_form', kwargs={'pk':self.yukiOwner.pk}))
		self.assertEqual(response.status_code, 200)

		self.client.logout()

		response = self.client.get(reverse('pet:owner_update_form', kwargs={'pk':self.yukiOwner.pk}))
		self.assertNotEqual(response.status_code, 200)
		self.assertEqual(response.status_code, 302)


	def test_owner_create_view_logged_in(self):
		self.client.login(username='Yuki', password='1234')
		response = self.client.get(reverse('pet:create_account'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Logout')


	def test_account_delete_view(self):
		# create user, login, logout
		self.client.login(username='Miles', password='1234')
		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk':self.milesOwner.pk}))
		self.assertEqual(response.status_code, 200)

		self.client.logout()
		self.miles.delete()

		self.client.login(username='Miles', password='1234')
		response = self.client.get(reverse('pet:owner_profile', kwargs={'pk':self.milesOwner.pk}))
		self.assertEqual(response.status_code, 302)


	def test_account_cancelled_view(self):
		response = self.client.get(reverse('pet:account_cancelled'))
		self.assertEqual(response.status_code, 200)


	def test_kennel_create_test_view(self):
		response = self.client.get(reverse('pet:manager_create_account'))
		self.assertEqual(response.status_code, 200)


	def test_kennel_profile_view_logged_in(self):
		self.client.login(username='Evelyn', password='1234')
		response = self.client.get(reverse('pet:manager_profile', kwargs={'pk':self.evelynKennel.pk}))
		self.assertEqual(response.status_code, 200)

		self.client.logout()

		response = self.client.get(reverse('pet:manager_profile', kwargs={'pk':self.evelynKennel.pk}))
		self.assertNotEqual(response.status_code, 200)
		self.assertEqual(response.status_code, 302)


	def test_kennel_update_view_logged_in(self):
		self.client.login(username='Evelyn', password='1234')
		response = self.client.get(reverse('pet:manager_update_form', kwargs={'pk':self.evelynKennel.pk}))
		self.assertEqual(response.status_code, 200)

		self.client.logout()

		response = self.client.get(reverse('pet:manager_update_form', kwargs={'pk':self.evelynKennel.pk}))
		self.assertNotEqual(response.status_code, 200)
		self.assertEqual(response.status_code, 302)


	def test_kennel_create_view_logged_in(self):
		self.client.login(username='Evelyn', password='1234')
		response = self.client.get(reverse('pet:manager_create_account'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Logout')

		self.client.logout()

		response = self.client.get(reverse('pet:manager_create_account'))
		self.assertEqual(response.status_code, 200)


	def test_index_logged_out_nav_bar_owner(self):
		response = self.client.get(reverse('pet:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '>Pet Owner</a></li>')


	def test_index_logged_out_nav_bar_manager(self):
		response = self.client.get(reverse('pet:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '>Pet Manager</a></li>')


	def test_index_logged_in_nav_bar(self):
		self.client.login(username='Evelyn', password='1234')
		response = self.client.get(reverse('pet:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '>My Account</a></li>')


	def test_login_logged_out_nav_bar_owner(self):
		response = self.client.get(reverse('pet:login'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '>Pet Owner</a></li>')


	def test_login_logged_out_nav_bar_manager(self):
		response = self.client.get(reverse('pet:login'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '>Pet Manager</a></li>')


	def test_login_logged_in_nav_bar(self):
		self.client.login(username='Evelyn', password='1234')
		response = self.client.get(reverse('pet:login'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '>My Account</a></li>')













