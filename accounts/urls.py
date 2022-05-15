from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', views.register, name='register')
]
