from django.contrib import admin
from django.urls import path,include
from users.views import CreateUser
urlpatterns=[
    path('registration/',CreateUser.as_view({'post':'create'}),name='registration')
]