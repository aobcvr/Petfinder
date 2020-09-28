from rest_framework import  viewsets
from rest_framework import permissions
from rest_framework.response import Response
from users.serialzer import CreateUserProfileSerializer

class CreateUser(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CreateUserProfileSerializer

    def create(self,request):
        serializer = CreateUserProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.create_user(validated_data=serializer.validated_data))