from django import forms
from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from .models import Pet, Owner, Kennel, Contact, Newsletter, Blog, IndexPhoto

class PetAdminForm(forms.ModelForm):
	food = forms.CharField( widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
	emergency = forms.CharField( widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
	care = forms.CharField( widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
	walk = forms.CharField( widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))

	class Meta:
		model = Pet 


class PetAdmin(admin.ModelAdmin):
	form = PetAdminForm
	readonly_fields = ('created', 'modified',)
	fieldsets = [ 
		('Info', 					{'fields': ['name', 'age', 'microchip_id']}),
		('Care Instructions', 		{'fields': ['food', 'emergency', 'care', 'walk']}), 
		('True | False Questions', 	{'fields': ['house_trained', 'spayed_or_neutered', 'barks']}), 
		('Picture', 	 			{'fields': ['picture']}),
		('Auto Fields', 			{'fields': ['created', 'modified', 'salt', 'short_salt', 'slug']}),
	]

class OwnerForm(forms.ModelForm):
	info = forms.CharField( widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))

	class Meta:
		model = Owner

class OwnerAdmin(admin.ModelAdmin):
	form = OwnerForm
	readonly_fields = ('created', 'modified',)
	filter_horizontal = ('pets',)
	fieldsets = [
		('Info',				{'fields': ['owner', 'name', 'email', 'contact', 'info', 'newsletter']}),
		('Picture', 	 		{'fields': ['picture']}),
		('Pets',				{'fields': ['pets']}),
		('Auto Fields', 		{'fields': ['created', 'modified', 'salt', 'short_salt', 'slug']}),
	] 


class KennelForm(forms.ModelForm):
	info = forms.CharField( widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))

	class Meta:
		model = Kennel 

class KennelAdmin(admin.ModelAdmin):
	form = KennelForm
	readonly_fields = ('created', 'modified',)
	filter_horizontal = ('owners',)
	fieldsets = [
		('Info',				{'fields': ['manager', 'name', 'kennel_name', 'contact', 'info', 'newsletter']}),
		('Picture', 	 		{'fields': ['picture']}),
		('Owners',				{'fields': ['owners']}),
		('Auto Fields', 		{'fields': ['created', 'modified', 'salt', 'short_salt', 'slug']}),
	]


class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact

class ContactAdmin(admin.ModelAdmin):
	form = ContactForm
	fieldsets = [
		('Info',				{'fields': ['name', 'email']}),
		('Message', 	 		{'fields': ['subject', 'message']}),
	]


class BlogForm(forms.ModelForm):
	story = forms.CharField( widget=forms.Textarea(attrs={'rows': 7, 'cols': 120}))

	class Meta:
		model = Blog 

class BlogAdmin(admin.ModelAdmin):
	form = BlogForm
	readonly_fields = ('created', 'modified',)
	fieldsets = [
		('Blog',				{'fields': ['author', 'title', 'story_description', 'story', 'link']}),
		('Picture', 	 		{'fields': ['picture']}),
		('Auto Fields', 		{'fields': ['created', 'modified', 'slug']}),
	]


class IndexPhotoForm(forms.ModelForm):
	slogan = forms.CharField( widget=forms.Textarea(attrs={'rows': 2, 'cols': 100}))

	class Meta:
		model = IndexPhoto 

class IndexPhotoAdmin(admin.ModelAdmin):
	form = IndexPhotoForm
	readonly_fields = ('created', 'modified',)
	fieldsets = [
		('Info',				{'fields': ['name', 'slogan', 'picture']}),
		('Auto Fields', 		{'fields': ['created', 'modified']}),
		]


admin.site.register(Pet, PetAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Kennel, KennelAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)
admin.site.register(Blog, BlogAdmin)
admin.site.register(IndexPhoto, IndexPhotoAdmin)








