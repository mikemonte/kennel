from django.conf.urls import patterns, url

from pet import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),

	# Login / Logout Views
	url(r'^accounts/login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^redirect_to_account/(?P<pk>\d+)/$', views.redirect_to_account, name='redirect_to_account'),

	# Owner Account Views
	url(r'^owner-create/$', views.OwnerCreateAccount.as_view(), name='create_account'),
	url(r'^owner-profile/(?P<pk>\d+)/$', views.OwnerProfileView.as_view(), name='owner_profile'),
	url(r'^owner-update/(?P<pk>\d+)/$', views.OwnerUpdateView.as_view(), name='owner_update_form'),
	url(r'^register-success/$', views.RegisterSuccessView.as_view(), name='register_success'),

	url(r'^owner-view-of-manager/(?P<pk>\d+)/(?P<salt>.+)/$', views.owner_view_of_manager, name='owner_view_of_manager'),
	url(r'^remove-kennel-connection/(?P<pk>\d+)/(?P<salt>.+)/$', views.remove_kennel_connection, name='remove_kennel_connection'),
	url(r'^add-kennel-connection/(?P<pk>\d+)/(?P<salt>.+)/$', views.add_kennel_connection, name='add_kennel_connection'),

	# Activate Account (for Owners and Managers) Views
	url(r'^activate/(?P<pk>\d+)/(?P<salt>.+)/$', views.activate, name='activate'),
	url(r'^activate-success/$', views.ActivateSuccessView.as_view(), name='activate_success'),

	# Reset Password Views
	url(r'^forgot-password/$', views.ForgotPasswordView.as_view(), name='forgot_password'),
	url(r'^reset-password/$', views.ResetPasswordView.as_view(), name='reset_password'),

	# Email Sent Views
	url(r'^contact-email-sent/$', views.ContactEmailSentView.as_view(), name='contact_email_sent'),
	url(r'^password-email-sent/$', views.PasswordEmailSentView.as_view(), name='password_email_sent'),
	url(r'^contact/$', views.ContactView.as_view(), name='contact'),

	# Manager Views
	url(r'^manager-create/$', views.ManagerCreateAccount.as_view(), name='manager_create_account'),
	url(r'^manager-profile/(?P<pk>\d+)/$', views.ManagerProfileView.as_view(), name='manager_profile'),
	url(r'^manager-update/(?P<pk>\d+)/$', views.ManagerUpdateView.as_view(), name='manager_update_form'),
	url(r'^manager-search/$', views.ManagerListView.as_view(), name='manager_list'),

	# Delete Account Views
	url(r'^delete-account/(?P<pk>\d+)/$', views.UserDeleteView.as_view(), name='user_delete_account'),
	url(r'^account-cancelled/$', views.AccountCancelledView.as_view(), name='account_cancelled'),

	# Manager Read-Only Views
	url(r'^read-only-owner-profile/(?P<pk>\d+)/(?P<salt>.+)/$', views.ro_owner_profile, name='ro_owner_profile'),
	url(r'^read-only-pet-profile/(?P<pk>\d+)/(?P<salt>.+)/$', views.ro_pet_profile, name='ro_pet_profile'),
	
	# Pet URL's for CreateView, UpdateView, and DetailView
	url(r'^pet-create/$', views.PetCreateView.as_view(), name='pet_create_form'),
	url(r'^pet-update/(?P<pk>\d+)/(?P<slug>[\w\d\-\_]+)/$', views.PetUpdateView.as_view(), name='pet_update_form'),
	url(r'^pet-detail/(?P<pk>\d+)/(?P<slug>[\w\d\-\_]+)/$', views.PetDetailView.as_view(), name='pet_detail'),
	url(r'^pet-delete/(?P<pk>\d+)/(?P<slug>[\w\d\-\_]+)/$', views.PetDeleteView.as_view(), name='pet_delete_form'),

	# Policy Views
	url(r'^privacy-policy/$', views.PrivacyPolicyView.as_view(), name='privacy_policy'),
	url(r'^terms-and-conditions/$', views.TermsAndConditionsView.as_view(), name='terms_and_conditions'),
	url(r'^mission-statement/$', views.MissionStatementView.as_view(), name='mission_statement'),
	url(r'^where-to-start/$', views.WhereToStartView.as_view(), name='where_to_start'),
	url(r'^sitemap/$', views.SitemapView.as_view(), name='sitemap'),	

	)
















