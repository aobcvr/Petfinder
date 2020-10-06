import logging
from django.http import HttpRequest
from django.utils import timezone
from listanimal.models import NewestLogFileContent

logger = logging.getLogger('rest.views')


class LoggerRequest:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response( request )
        if response.status_code==401:
            logger.error(msg='Попытка пройти по ссылке без авторизации {},{} \n'
                        .format(str(HttpRequest.get_full_path(request)),
                        str(timezone.now())))
            log_db = open('logger/request_err.log','r').readlines()[-100:-1]
            index = 0
            for log in log_db:
                log_db[index] = log.rstrip()
                index += 1
            log_db.reverse()
            NewestLogFileContent.objects.update_or_create(
                log_filename='create.logger',
                defaults={'content':log_db})
        return response