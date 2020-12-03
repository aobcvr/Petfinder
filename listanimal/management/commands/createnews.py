import vk_api
import logging
from listanimal.parseranimal import RtNewsAnimalParser
from django.core.management.base import BaseCommand
from listanimal.models import AnimalNews
from django.conf import settings

from listanimal.management.service.vk_wall_post_news import VkWallPostNews
from listanimal.management.service.send_mail import SendMail
logger = logging.getLogger('commands.createnews')
log_db = open('logger/news.log', 'r')


class Command(BaseCommand):
    def handle(self, *args, **options):

        self.createnews()

    def createnews(self):

        summ_new_news = ''
        group_id = settings.GROUP_ID
        vk_session = vk_api.VkApi(token=settings.ACESS_TOKEN_ATTACHEMENT)
        upload_url = vk_session.method('photos.getWallUploadServer',
                                       {'group_id': group_id,
                                        'v': 5.95})['upload_url']
        news = RtNewsAnimalParser.rt_news_animal(self)
        for animal_news in news:
            create_object, is_created = AnimalNews.objects.get_or_create(
                heading=animal_news['heading'], defaults=animal_news)
            if is_created:
                    VkWallPostNews.vk_wall_news(self, animal_news,
                                                summ_new_news, group_id,
                                                vk_session, upload_url)
                    summ_new_news += '\n' + ' Заголовок статьи:' + \
                                     animal_news['heading']
        SendMail.send_news(self, summ_new_news, animal_news)