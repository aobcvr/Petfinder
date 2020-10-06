from rest_framework import serializers
from listanimal.models import CustomUser
from rest_framework.authtoken.models import Token

class CreateUserProfileSerializer(serializers.ModelSerializer):
    '''
    Создает пользователя с password,username
    '''
    password2 = serializers.CharField( style={'input_type': 'password'},max_length=200)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'password2']

    def create_user(self,validated_data):
            username = self.validated_data['username']
            password = self.validated_data['password']
            CustomUser.objects.create(password=password, username=username)
            Token.objects.create(user=CustomUser.objects.get(username=username))