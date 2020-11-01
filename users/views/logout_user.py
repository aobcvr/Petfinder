from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import logout


class LogoutUser(viewsets.ViewSet):
    '''
    выход пользователя из аккаунта
    '''

    def logout_user(self,request):
        logout(request)
        return Response({'status':'successful logout'})