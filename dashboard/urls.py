from django.conf.urls import patterns, include, url
from dashboard.views import MainView

urlpatterns = patterns('',
	url(r'^$', MainView.as_view()),
)

