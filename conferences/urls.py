from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<id>\d+)-(?P<slug>[-\w]+)/$', views.ConferenceDetailView.as_view(), name='conference_detail'),
    url(r'^$', views.conference_list, name='conference_list'),
]