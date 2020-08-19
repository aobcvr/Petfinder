from django.http import HttpRequest
from django.utils import timezone

from rest.serializer import UrlAnimalAdvertSerializer
from listanimal.models import AnimalInfo
from listanimal.models import NewestLogFileContent
from rest.serializer.serializers_animal import AnimalInfoSerializer

from rest_framework import viewsets
from rest_framework import permissions

from drf_yasg.views import get_schema_view

import logging
logger = logging.getLogger('rest.views')
SchemaView=get_schema_view()

class LoggerRequest:

    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self, request):
        response=self.get_response(request)
        if response.status_code==401:
            logger.error(msg='Попытка пройти по ссылке без авторизации {},{} \n'.format(str(HttpRequest.get_full_path(request)),str(timezone.now())))
            log_db=open('listanimal/logger/request_err.log','r').readlines()[-100:-1]
            index=0
            for log in log_db:
                log_db[index]=log.rstrip()
                index+=1
            log_db.reverse()
            NewestLogFileContent.objects.update_or_create(log_filename='create.logger',defaults={'content':log_db})
        return response

class AnimalAdvertisementView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AnimalInfoSerializer
    queryset = AnimalInfo.objects.all()

    def list(self,request, *args, **kwargs ):
        serializer = UrlAnimalAdvertSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        self.queryset = serializer.search_advert()
        return super().list(self, request, *args, **kwargs)