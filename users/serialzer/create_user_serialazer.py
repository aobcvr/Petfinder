from rest_framework import serializers
from listanimal.models import CustomUser
from rest_framework.response import Response
from django.http import HttpResponse
class CreateUserProfileSerializer(serializers.ModelSerializer):
    '''
    Создает пользователя с email,password,username
    '''
    password2 = serializers.CharField(max_length=200)

    class Meta:
        model = CustomUser
        fields = ['username','password','email','password2']

    def create_user(self, validated_data):
        if self.validated_data['password'] != self.validated_data['password2']:
            return 'пароли не совпадают'
        else:
            username = self.validated_data['username']
            password = self.validated_data['password']
            email = self.validated_data['email']
            CustomUser.objects.create(password=password,username=username,email=email)
            return 'created'
        '''
        создание пользователя
        '''

