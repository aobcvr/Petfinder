from rest_framework.views import APIView
from .serializer.serializers_animal import AnimalInfoSerializer,AnimalTypeSerializer,AnimalColorSerializer
from .serializer import AnimalNewsSerializer
from listanimal.models import AnimalInfo,AnimalColor,AnimalType
from rest_framework.response import Response
from .serializer import UrlAnimalNewsSerializer
from .serializer import UrlAnimalAdvertSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpRequest
from drf_yasg.views import get_schema_view
from listanimal.models import NewestLogFileContent
from django.utils import timezone
import logging
from datetime import datetime
logger = logging.getLogger('rest.views')

SchemaView=get_schema_view()

class LoggerRequest:

    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self, request):
        response=self.get_response(request)
        if response.status_code==401:
            logger.error(msg='Попытка пройти по ссылке без авторизации {},{}'.format(str(HttpRequest.get_full_path(request)),str(timezone.now())))
            log_db=open('rest/request_err.log','r').readlines()[-100:-1]
            index=0
            for log in log_db:
                log_db[index]=log.rstrip()
                index+=1
            log_db.reverse()
            NewestLogFileContent.objects.update_or_create(log_filename='create.logger',defaults={'content':log_db})
        return response


class AnimalNewsView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UrlAnimalNewsSerializer

    def get(self,request, *args, **kwargs ):
            serializer = self.serializer_class(data=request.GET)
            serializer.is_valid(raise_exception=True)
            response = serializer.search_news()
            return Response(AnimalNewsSerializer(response, many=True).data)


class AnimalAdvertisementView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AnimalInfoSerializer
    queryset = AnimalInfo.objects.all()

    def list(self,request, *args, **kwargs ):
        serializer = UrlAnimalAdvertSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        self.queryset = serializer.search_advert()
        return super().list(self, request, *args, **kwargs)


class AnimalAdvertisementTupeView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self,request):
        type = AnimalType.objects.all()
        serializer=AnimalTypeSerializer(type,many=True)
        return Response(serializer.data)


class AnimalAdvertisementColorView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self,request):
        color = AnimalColor.objects.all()
        serializer=AnimalColorSerializer(color,many=True)
        return Response(serializer.data)


class FavoritAnimal(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self,request):
            queriset=request.user.favorit_animal.all()
            private_data = AnimalInfoSerializer(queriset, many=True).data
            return Response(private_data)
