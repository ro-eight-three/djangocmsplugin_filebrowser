from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/(?P<path>.*)$', views.ListPathView.as_view(), name='list'),
]
