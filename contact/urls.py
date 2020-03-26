from django.contrib import admin
from django.conf.urls import url, include




from .views import emailView, SuccessView

urlpatterns = [
    url(r'^email/', emailView, name='email'),
    url(r'^success/', SuccessView, name='success'),
]