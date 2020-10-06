from django.contrib import admin
from django.urls import path,include
from users.views import CreateUser,EmailAuth


urlpatterns=[
    path('registration/',CreateUser.as_view({'post':'create'}),name='registration'),
    path('email_auth/',EmailAuth.as_view({'post':'create'}),name='email_auth'),
]