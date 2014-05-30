from django.conf.urls import *
from views import weixin
from views import weixin_test

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin  
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^weixin/$',weixin),
    url(r'^weixin/test/$',weixin_test),
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'weixin.views.home', name='home'),
    # url(r'^weixin/', include('weixin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:    
)
