from django.contrib import admin
from django.urls import path,include
from users.views import CreateUser,EmailAuth
from rest_framework import routers
router = routers.SimpleRouter()

urlpatterns=[
    path('registration/',CreateUser.as_view({'post':'create'}),name='registration'),
    path('email_auth/',EmailAuth.as_view({'post':'create','get':'get'}),name='email_auth'),
]