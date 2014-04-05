import django
from django.contrib.auth.models import Group, Permission, User 
from django.contrib.contenttypes.models import ContentType 

from .models import Pet, Owner, Kennel

def add_owner_group():
	owner_users = Group(name='Owner Users')
	owner_users.save()
	return owner_users

def add_kennel_group():
	kennel_users = Group(name='Kennel Users')
	kennel_users.save()
	return kennel_users


def add_owner_permissions():
	owner_ct = ContentType.objects.get(app_label='pet', model='owner')
	is_owner = Permission(name='Is Owner', codename='is_a_owner', content_type=owner_ct)
	is_owner.save()
	return is_owner

def add_kennel_permissions():
	kennel_ct = ContentType.objects.get(app_label='pet', model='kennel')
	is_kennel = Permission(name='Is Kennel', codename='is_a_kennel', content_type=kennel_ct)
	is_kennel.save()
	return is_kennel

def give_perm_to_owner_group():
	owner_users = Group.objects.get(name='Owner Users')
	owner_users.permissions.add(is_owner)
	return owner_users

def give_perm_to_kennel_group():
	kennel_users = Group.objects.get(name='Kennel Users')
	kennel_users.permissions.add(is_kennel)
	return kennel_users


def add_owner_perm(pk):
	"""
	working functions used in pet.views.OwnerCreateAccount
	"""
	user = User.objects.get(pk=pk)
	owner_users = Group.objects.get(name='Owner Users')
	user.groups.add(owner_users)
	user.save()
	return user

def add_kennel_perm(pk):
	"""
	working functions used in pet.views.ManagerCreateAccount
	"""
	user = User.objects.get(pk=pk)
	kennel_users = Group.objects.get(name='Kennel Users')
	user.groups.add(kennel_users)
	user.save()
	return user















