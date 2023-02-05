from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('text/', views.encrypt_text, name='encrypt'),
    path('decrypt/', views.decrypt, name='decrypt'),
]