from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^project-about/$', views.project_about, name='project-about'),
    url(r'^project-platform/$', views.project_platform, name='project-platform'),
    url(r'^project-model/$', views.project_model, name='project-model'),
    url(r'^project-route/$', views.project_route, name='project-route'),
]
