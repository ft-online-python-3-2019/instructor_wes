from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create/$', views.create, name="create"),
    url(r'^(?P<lecture_id>\d+)/$', views.show, name="show"),
    url(r'^(?P<lecture_id>\d+)/edit/$', views.edit, name="edit"),
    url(r'^(?P<lecture_id>\d+)/update/$', views.update, name="update"),
    url(r'^(?P<lecture_id>\d+)/delete/$', views.destroy, name="destroy"),
]