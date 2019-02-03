from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.NewsListView.as_view(), name='news'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.NewsDetailView.as_view(), name='news_detail'),

]
