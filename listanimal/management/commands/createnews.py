import vk_api
import logging
import time
import os
import requests
from listanimal.parseranimal import RtNewsAnimalParser
from django.core.management.base import BaseCommand
from listanimal.models import NewestLogFileContent, AnimalNews
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

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
        Command.send_news(self, summ_new_news, animal_news)

    def send_news(self, summ_new_news, animal_news):
        # send_news - отправляет сообщения пользователям сервиса
        if summ_new_news != '':
            send_mail('новая новость ', summ_new_news,
                      settings.EMAIL_HOST_USER, ['paveligin1861@gmail.com'],
                      fail_silently=False)
        elif summ_new_news == '':
            send_mail('нет новостей', 'новостей нет',
                      settings.EMAIL_HOST_USER, ['paveligin1861@gmail.com'],
                      fail_silently=False)
        else:
            logger.error(msg='Ошибка отправки новости на ящик:{},'
                             '{}'.format(animal_news['description_news'],
                                         timezone.now()))
            NewestLogFileContent.objects.get_or_create(
                defaults={'log_filename': 'commands.createnews',
                          'content': log_db.read()})


class VkWallPostNews():
    """
    Класс предоставляет функции для выкладывания новостей
    с разным содержанием, а также каждая функция просматривает
    наличие или отсутствие основоного текста(main_text)
    """
    def vk_wall_news(self, animal_news, group_id, vk_session, upload_url):
        # vk_wall_news - осуществляет определение через какую функцию
        # будет обрабатываться новость
        if animal_news.get('url_media', None) is not None:
            if animal_news['url_media'].endswith('.mp4'):
                VkWallPostNews.vk_wall_news_mp4(self,
                                                animal_news,
                                                group_id,
                                                vk_session, )
            else:
                VkWallPostNews.vk_wall_news_photo(self, animal_news,
                                                  upload_url, vk_session,
                                                  group_id)
        elif animal_news.get('gallery_img', None) is not None:
            VkWallPostNews.vk_wall_news_gallery_img(self, animal_news,
                                                    upload_url, vk_session,
                                                    group_id)
        else:
            VkWallPostNews.vk_wall_without_media_file(self, animal_news,
                                                      vk_session, group_id)

    def vk_wall_news_mp4(self, animal_news, group_id, vk_session):
        # vk_wall_news_mp4 - выкладывает новость, если в ней есть
        # mp4 файл в новости

        news = {'owner_id': -group_id, 'from_group': 1, 'message': '{}\n'
                'Ссылка на оригинал:{}\n Вложение:{}\n{}\n{}\n '
                'Ссылка на видео:{}'.format(
                                            animal_news['time_post'],
                                            animal_news['url_news'],
                                            animal_news.get('main_text', None),
                                            animal_news['description_news'],
                                            animal_news['heading'],
                                            animal_news['url_media'])}
        if animal_news.get('url_media', None) is not None:
            vk_session.method('wall.post', news)

    def vk_wall_news_photo(self, animal_news, upload_url, vk_session, group_id):
        # vk_wall_news_photo - выкладывает новость, при наличии в ней
        # 1-й фотографии в новости
        photo = requests.get(animal_news['url_media'])
        images = open('images.jpg', 'wb')
        images.write(photo.content)
        request = requests.post(upload_url,
                                files={'file': open('images.jpg', 'rb')})
        save_wall_photo = vk_session.method('photos.saveWallPhoto',
                                            {'group_id': group_id, 'v': 5.95,
                                             'photo': request.json()['photo'],
                                             'server': request.json()['server'],
                                             'hash': request.json()['hash']})
        saved_photo = 'photo' + str(save_wall_photo[0]['owner_id']) \
                      + '_' + str(save_wall_photo[0]['id'])
        news = {'owner_id': -group_id,
                'from_group': 1,
                'message': '{}\nСсылка на оригинал:{}\n'
                'Вложение:{}\n{}\n{}'.format(
                                            animal_news['time_post'],
                                            animal_news['url_news'],
                                            animal_news.get('main_text', None),
                                            animal_news['description_news'],
                                            animal_news['heading']),
                           'attachments': saved_photo}
        vk_session.method('wall.post', news)
        os.remove('images.jpg')

    def vk_wall_news_gallery_img(self, animal_news, upload_url, vk_session, group_id):
        # vk_wall_news_gallery_img - выкладывает новость при наличии
        # галлереи фотографий в новости
        saved_gallery = ''
        for one_img in animal_news['gallery_img']:
            photo = requests.get(one_img.replace(' ', ''))
            images = open('images.jpg', 'wb')
            images.write(photo.content)
            time.sleep(5)
            request = requests.post(upload_url,
                                    files={'file': open('images.jpg', 'rb')})
            save_wall_photo = vk_session.method('photos.saveWallPhoto',
                                                {'group_id': group_id, 'v': 5.95,
                                                 'photo': request.json()['photo'],
                                                 'server': request.json()['server'],
                                                 'hash': request.json()['hash']})
            saved_photo = 'photo' + str(save_wall_photo[0]['owner_id']) \
                          + '_' + str(save_wall_photo[0]['id'])
            saved_gallery += saved_photo + ','
            os.remove('images.jpg')
        news = {'owner_id': -group_id, 'from_group': 1,
                'attachments': saved_gallery,
                'message': '{}\nСсылка на оригинал:{}\n'
                'Вложение:{}\n{}\n{}'.format(
                                            animal_news['time_post'],
                                            animal_news['url_news'],
                                            animal_news.get('main_text', None),
                                            animal_news['description_news'],
                                            animal_news['heading'])}
        vk_session.method('wall.post', news)

    def vk_wall_without_media_file(self, animal_news, vk_session, group_id):
        # vk_wall_without_media_file - выкладывает новость при
        # отсутствии медиафайлов
        news = {'owner_id': -group_id,
                'from_group': 1, 'message': '{}\nСсылка на оригинал:{}\n'
                'Вложение:{}\n{}\n{}'.format(
                                            animal_news['time_post'],
                                            animal_news['url_news'],
                                            animal_news.get('main_text', None),
                                            animal_news['description_news'],
                                            animal_news['heading'])}
        vk_session.method('wall.post', news)
