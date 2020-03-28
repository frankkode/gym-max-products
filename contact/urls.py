from django.contrib import admin
from django.urls import path

from .views import emailView, SuccessView

urlpatterns = [
    path('email/', emailView, name='email'),
    path('success/', SuccessView, name='success'),
]