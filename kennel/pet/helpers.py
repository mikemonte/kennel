import random

from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def short_salt():
	ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	chars=[]
	for i in range(8):
		chars.append(random.choice(ALPHABET)) 
	return "".join(chars)


def salt():
	ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	chars=[]
	for i in range(16):
		chars.append(random.choice(ALPHABET)) 
	return "".join(chars)


def signup_email(username, email, pk, signup_link):
	subject, from_email, to = 'Site Registration', settings.DEFAULT_FROM_EMAIL, email
	text_content = 'Click on link to finish registration'
	html_content = render_to_string('pet/html_email.html', {'username': username, 'pk':pk, 'signup_link':signup_link})
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	return msg 


def forgot_password_email(username, email, temp_password):
	subject, from_email, to = 'Temporary Password Reset', settings.DEFAULT_FROM_EMAIL, email
	text_content = 'Click on link to reset your password'
	html_content = render_to_string('pet/password_reset_email.html', {'username': username, 'temp_password':temp_password})
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	return msg 	

def account_cancelled_email(username, email):
	subject, from_email, to = 'Pet Stayz: Account Cancelled', settings.DEFAULT_FROM_EMAIL, email
	text_content = 'Dear {0}, your account has been cancelled.  Thank you and we hope to see you again sometime.'.format(username)
	html_content = render_to_string('pet/account_cancelled_email.html', {'username': username})
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	return msg 	


def contact_email(name, email, subject, message):
	subject, from_email, to = 'Pet Stayz: Contact Email from {0}'.format(name), settings.DEFAULT_FROM_EMAIL, settings.DEFAULT_FROM_EMAIL
	text_content = 'Name: {0}; Email {1}; Subject {2}; Message {3}'.format(name, email, subject, message)
	html_content = render_to_string('pet/html_contact_email.html', {'name':name, 'email':email, 'subject':subject, 'message':message})
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	return msg 	











