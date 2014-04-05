from django import forms 
from django.contrib.auth.models import User

from .models import Pet, Owner, Kennel, Contact, Newsletter


class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('email',)

 
class PetForm(forms.ModelForm):

	class Meta:
		model = Pet
		fields = ('name', 'age', 'food', 'emergency', 'care', 'walk', 'microchip_id', 'picture', 'house_trained', 'spayed_or_neutered', 'barks',)
		widgets = {
			'food': forms.Textarea(attrs={'cols': 10, 'rows': 6}),
			'emergency': forms.Textarea(attrs={'cols': 10, 'rows': 6}),
			'care': forms.Textarea(attrs={'cols': 10, 'rows': 6}),
			'walk': forms.Textarea(attrs={'cols': 10, 'rows': 6}), 
		}
 
 
class Login(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def is_active_check(self): 
		username = self.cleaned_data['username']
		try:
			user = User.objects.get(username=username) 
			if user is not None and user.is_active == False:
				raise forms.ValidationError("Your account hasn't been activated yet.  Please follow the link in your email to validate your account")
		except:
			raise forms.ValidationError("Username and password do not match")
		return username

class Owner_Register(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError("That username is already taken")
		return username


class Kennel_Register(forms.Form):
	username = forms.CharField()
	kennel_name = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError("That user is already taken")
		return username


class Owner_Info_Form(forms.ModelForm):

	class Meta:
		model = Owner
		fields = ('name', 'email', 'contact', 'info', 'picture', 'newsletter',)
		widgets = {
			'info': forms.Textarea(attrs={'cols': 10, 'rows': 6}),
		}

class Manager_Info_Form(forms.ModelForm):

	class Meta:
		model = Kennel 
		fields = ('name', 'kennel_name', 'email', 'contact', 'info', 'picture', 'newsletter',)
		widgets = {
			'info': forms.Textarea(attrs={'cols': 10, 'rows': 6}),
		}


class NewsletterForm(forms.ModelForm):

	class Meta:
		model = Newsletter
		fields = ('email',)


class Forgot_Password(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()


class Reset_Password(forms.Form):
	username = forms.CharField()
	temp_password = forms.CharField()
	new_password = forms.CharField(widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data['username']
		if not User.objects.filter(username=username).exists():
			raise forms.ValidationError("Invalid Username")
		return username


class ContactForm(forms.ModelForm):

	# def __init__(self, *args, **kwargs):
	# 	super(ContactForm, self).__init__(*args, **kwargs)
	# 	self.fields['subject'].required=False 

	class Meta:
		model = Contact  
		fields = ('name', 'email', 'subject', 'message',)
		widgets = {
			'message': forms.Textarea(attrs={'cols': 10, 'rows': 6}),
		}







