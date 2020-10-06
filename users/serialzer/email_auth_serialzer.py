from listanimal.models import CustomUser
from users.models import EmailAuth

from rest_framework import serializers

from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpRequest

from uuid import uuid4
class EmailAuthSerialazer(serializers.ModelSerializer):


    class Meta:
        model = CustomUser
        fields = ['email','password']

    def email_auth(self,validated_data,request):
        key=uuid4()
        send_mail('Подтверждение email', 'Подтвердите email перейдя по ссылке 127.0.0.1:8000{}?key={}'.format(str(HttpRequest.get_full_path(request)),key), settings.EMAIL_HOST_USER, [self.validated_data['email']],
                  fail_silently=False)
        EmailAuth.objects.create(user=request.user,key=key,email_e=self.validated_data['email'])

class EmailSaveSerialazer(serializers.Serializer):
    key = serializers.CharField(max_length=200)

    def email_save(self,validated_data):
        norm_uuid=EmailAuth.objects.get(key=self.validated_data['key'])
        norm_uuid.user(email=norm_uuid.email_e)
