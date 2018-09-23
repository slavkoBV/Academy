from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProjectListView.as_view(), name='projects'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
]
