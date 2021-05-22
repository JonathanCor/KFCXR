__author__ = 'Jonathan Corvers'

from django.urls import path

from . import views


app_name = 'main_page'
urlpatterns = [
    path('', views.index, name='index'),
    path('setLanguage/<str:language>/', views.set_session_language, name='setLanguage'),
]
