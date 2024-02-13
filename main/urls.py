from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index_page),
    path('auth/<str:type>', request_auth)
]
