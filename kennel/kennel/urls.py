from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kennel.views.home', name='home'),
    # url(r'^kennel/', include('kennel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^aronysidoro/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include('admin_honeypot.urls')), 
    url(r'^aronysidoro/', include(admin.site.urls)),

    url('', include('pet.urls', namespace='pet'))
)
