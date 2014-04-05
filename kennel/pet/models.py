# import bcrypt
import datetime
import random

from django.db import models
from django.contrib.auth.models import User
from django.forms import Textarea
from django.core.validators import MaxLengthValidator
from django.utils.baseconv import base36
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

from .helpers import short_salt, salt 


def pet_content_file_name(instance, filename):
	return '/'.join(['pet_pictures', filename])


def owner_content_file_name(instance, filename): 
	return '/'.join(['owner_pictures', filename])


def manager_content_file_name(instance, filename):
	return '/'.join(['manager_pictures', filename])

def blog_content_file_name(instance, filename):
	return '/'.join(['blog_pictures', filename])

def index_content_file_name(instance, filename):
	return '/'.join(['index_pictures', filename])


class PetAppSetupModel(models.Model):
	"""
	An abstract class that provides self-
	updating 'created' and 'modified' fields.
	In addition to other fields needed by all Models in Pet App
	"""
	# Required
	name = models.CharField(max_length=55)
	# Auto Fields
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	salt = models.CharField(max_length=75)
	short_salt = models.CharField(max_length=75)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
			self.salt = salt() 
			self.short_salt = short_salt()
		super(PetAppSetupModel, self).save(*args, **kwargs)

	class Meta:
		abstract = True


class Pet(PetAppSetupModel):
	food = models.CharField(max_length=1000, verbose_name='Feeding Instructions')
	emergency = models.CharField(max_length=1000, verbose_name='Emergency Contact')
	# Optional Fields
	age = models.PositiveIntegerField(max_length=2, null=True, blank=True, default=1)
	care = models.CharField(max_length=1000, verbose_name='Care Instructions', blank=True)
	walk = models.CharField(max_length=1000, verbose_name='Walking Instructions', blank=True)
	picture = models.ImageField(upload_to=pet_content_file_name, null=True, verbose_name="Picture", blank=True)
	microchip_id = models.CharField(max_length=55, blank=True)
	# True / False Fields
	house_trained = models.BooleanField(default=False, help_text='Yes')
	spayed_or_neutered = models.BooleanField(default=False, help_text='Yes')
	barks = models.BooleanField(default=False, help_text='Yes')

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('pet:pet_detail', kwargs={'pk': self.pk, 'slug': self.slug})

	class Meta:
		ordering = ['name']


class Owner(PetAppSetupModel):
	owner = models.ForeignKey(User)
	pets = models.ManyToManyField(Pet)
	# Optional Fields
	email = models.EmailField(max_length=100, blank=True)
	contact = models.CharField(max_length=50, verbose_name='Contact PH#', blank=True)
	info = models.CharField(max_length=1000, verbose_name='Additional Information', blank=True)
	picture = models.ImageField(upload_to=owner_content_file_name, null=True, verbose_name="Picture", blank=True)
	# True / False Fields
	newsletter = models.BooleanField(default=False, help_text='Yes')

	def save(self, *args, **kwargs):
		if not self.name:
			self.name = User.objects.get(username=self.owner).username
		if not self.email:
			self.email = User.objects.get(username=self.owner).email
		super(Owner, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name 

	def get_absolute_url(self):
		return reverse('pet:owner_profile', kwargs={'pk': self.pk, 'slug': self.slug})

	def activated_in_time(self):
		now = timezone.now()
		return now >= self.created >= now - datetime.timedelta(days=1)

	class Meta:
		permissions = (
			('is_owner', 'Is Owner'),
		)


class Kennel(PetAppSetupModel):
	manager = models.ForeignKey(User)
	owners = models.ManyToManyField(Owner)
	# Required
	kennel_name = models.CharField(max_length=75)
	# Optional
	email = models.EmailField(max_length=100, blank=True)
	contact = models.CharField(max_length=50, verbose_name='Contact PH#', blank=True)
	info = models.CharField(max_length=1000, verbose_name='Additional Information', blank=True)
	picture = models.ImageField(upload_to=manager_content_file_name, null=True, verbose_name="Picture", blank=True)
	# True / False Fields
	newsletter = models.BooleanField(default=False, help_text='Yes')

	def save(self, *args, **kwargs):
		if not self.name:
			self.name = User.objects.get(username=self.manager).username
		if not self.email:
			self.email = User.objects.get(username=self.manager).email
		super(Kennel, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.kennel_name 

	def activated_in_time(self):
		now = timezone.now()
		return now >= self.created >= now - datetime.timedelta(days=1)

	class Meta:
		permissions = (
			('is_kennel', 'Is Kennel'),
		)


class Contact(models.Model):

	name= models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	subject = models.CharField(max_length=100)
	message = models.CharField(max_length=1500)

	def __unicode__(self):
		return '{0} - {1}'.format(self.name, self.email) 

	class Meta:
		ordering = ['name', 'email']


class Newsletter(models.Model):

	email = models.EmailField(max_length=100)

	def __unicode__(self):
		return self.email

	class Meta:
		ordering = ['email']


class Blog(models.Model):

	# Join
	author = models.ForeignKey(User)
	# Auto Fields
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	slug = models.SlugField(blank=True)
	# Blog specific fields
	title = models.CharField(max_length=100)
	story_description = models.CharField(max_length=255)
	story = models.CharField(max_length=5000)
	link = models.URLField(blank=True)
	picture = models.ImageField(upload_to=blog_content_file_name, verbose_name="Picture")

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Blog, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-modified']

	class Meta:
		permissions = (
			('is_blogger', 'Is Blogger'),
		)


class IndexPhoto(models.Model):

	# Auto Fields
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	# Normal Fields
	name = models.CharField(max_length=55)
	picture = models.ImageField(upload_to=index_content_file_name, verbose_name="Picture")
	slogan = models.CharField(max_length=255, blank=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['-modified']



