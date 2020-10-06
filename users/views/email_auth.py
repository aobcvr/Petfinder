from rest_framework import  viewsets, permissions
from users.serialzer import EmailAuthSerialazer
from rest_framework.response import Response

class EmailAuth(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self,request):

        serialazer = EmailAuthSerialazer(data=request.data)
        serialazer.is_valid(raise_exception=True)
        if serialazer.validated_data['password'] != request.user.password:
            return Response({'status':'неправильынй пароль'})
        serialazer.email_auth(validated_data=serialazer.validated_data,request=request)
        return Response({'status':'check your email'})

    def get(self,request):
        pass


    


