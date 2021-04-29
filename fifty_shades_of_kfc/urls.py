__author__ = 'Jonathan Corvers'

from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index')
]
