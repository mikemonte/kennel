
"""
Selenim Tests 
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



# class MySeleniumTests(LiveServerTestCase):
#     # fixtures = ['user-data.json']

#     @classmethod
#     def setUpClass(cls):
#         cls.selenium = WebDriver()
#         super(MySeleniumTests, cls).setUpClass()

#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super(MySeleniumTests, cls).tearDownClass()

#     def test_login(self):
#         self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
#         username_input = self.selenium.find_element_by_name("username")
#         username_input.send_keys('Yuki')
#         password_input = self.selenium.find_element_by_name("password")
#         password_input.send_keys('1234')
#         self.selenium.find_element_by_xpath('//input[@value="Login"]').click()





