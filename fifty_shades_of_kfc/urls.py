__author__ = 'Jonathan Corvers'

from django.urls import path

from . import views


app_name = 'fifty_shades_of_kfc'
urlpatterns = [
    path('', views.index, name='index'),
    path('setLanguage/<str:language>/', views.set_session_language, name='setLanguage'),
    path('viewCategory/<str:category_reference>/', views.view_malpractice_category, name='viewCategory'),
    path('viewCategory/<str:category_reference>/setLanguage/<str:language>/', views.set_session_language_in_category, name='setLanguageCategory'),
]
