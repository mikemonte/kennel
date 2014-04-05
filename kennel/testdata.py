import random

from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import Group, Permission, User 
from django.contrib.contenttypes.models import ContentType 

from pet.models import Pet, Owner, Kennel


def create_user(user_name):
	user = User.objects.create_user(user_name, email='pyaaron@gmail.com', password='1234')
	return user 

class CreateTestData(object):

	def __init__(self):
		# Create Users
		self.evelyn = create_user('Evelyn')
		self.yuki = create_user('Yuki')
		self.lauren = create_user('Lauren') 
		self.dad = create_user('Dad')
		self.miles = create_user('Miles')

		# Create Pets
		self.bobbi = Pet.objects.create(name='Bobbi', age='1', food='dry food', emergency='tropicana')
		self.dino = Pet.objects.create(name='Dino', age='1', food='dry food', emergency='tropicana')
		self.hama = Pet.objects.create(name='Hama', age='1', food='dry food', emergency='tropicana')

		# Create Kennels
		self.evelynKennel = Kennel.objects.create(kennel_name="Evenlyn's Kennel", manager=self.evelyn, name=self.evelyn.username)
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












		