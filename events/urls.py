from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^profile/(?P<id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^event/(?P<id>[0-9]+)/$', views.event_detail, name='event_detail'),
    url(r'^register$', views.register, name='register'),
]