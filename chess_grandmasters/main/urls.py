from django.urls import path
from . import views

urlpatterns = [
    path('', views.carousel, name='carousel'),
    path('cards/', views.cards, name='cards'),
    path('accordion/', views.accordion, name='accordion'),
    path('contacts/', views.contacts, name='contacts'),
]