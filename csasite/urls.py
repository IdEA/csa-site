from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from dashboard.api import SensorDataResource
from csasite.views import MainView

csa_api_v1 = Api(api_name='v1')
csa_api_v1.register(SensorDataResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'csasite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^admin/', include(admin.site.urls)),
   url(r'^api/', include(csa_api_v1.urls)),
   url(r'^dash/', include('dashboard.urls')),
   url(r'^$', MainView.as_view()),
)
