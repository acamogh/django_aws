from django.conf.urls import url,include
from django.contrib import admin

from . import views



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^addPost/$', views.add_post, name='add_post'),
    url(r'^about/$', views.about, name='about'),
    url(r'^editPost/(?P<id>\d+)/$', views.edit_post, name='edit_post'),
    url(r'^deletePost/(?P<id>\d+)/$', views.delete_post, name='delete_post'),

]
