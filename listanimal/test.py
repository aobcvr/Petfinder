from unittest.mock import patch
from unittest import TestCase
from listanimal.parseranimal import RtNewsAnimalParser
from listanimal.management.commands.createanimal import Command
from bs4 import BeautifulSoup as bs


class MockTestParserAnimal(TestCase):
    parser = RtNewsAnimalParser()

    @patch('listanimal.parseranimal.RtNewsAnimalParser.rt_news_animal')
    def test_parser_rt_news(self,mock_rt_news_animal):
        base_url = 'https://russian.rt.com'
        list_news = open('listanimal/test/html_file_test/list_news.html','r').read()
        soup = bs(list_news, 'html.parser')
        all_list_news = soup.find_all('div', 'card__heading_all-new')
        for list_news in all_list_news:
            url_news = list_news('a', 'link_color')
            for url_new in url_news:
                url_new = base_url + url_new['href']
                news = open('listanimal/test/html_file_test/news.html','r').read()
                soup_url_new = bs(news, 'html.parser')
                heading = soup_url_new.find('div', 'article__summary').text
                time_post = soup_url_new.find('time', 'date')['datetime']
                set_news = {'url_news': url_new,
                            'description_news': list_news.text.strip(),
                            'heading': heading.strip(),
                            'time_post': time_post}
        mock_rt_news_animal.return_value = set_news
        result = self.parser.rt_news_animal()
        self.assertEqual(result, set_news)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.add_main_text')
    def test_add_main_text(self, mock_add_main_text):
        news = open('listanimal/test/html_file_test/news.html', 'r').read()
        soup_url_new = bs(news, 'html.parser')
        main_text = soup_url_new.find('div', 'article__text')
        if main_text is not None:
            main_text_find_all = main_text.find_all('p')
            full_text = ''
            for main_text_p in main_text_find_all:
                full_text += main_text_p.text
        mock_add_main_text.return_value = main_text
        result = self.parser.add_main_text()
        self.assertEqual(result, main_text)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.add_url_media')
    def test_add_url_media(self, mock_add_url_media):
        news = open('listanimal/test/html_file_test/news.html', 'r').read()
        soup_url_new = bs(news, 'html.parser')
        url_media = soup_url_new.find('img', 'article__cover-image')['src']
        mock_add_url_media.return_value = url_media
        result = self.parser.add_url_media()
        self.assertEqual(result, url_media)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.add_mediaplayer_mp4')
    def test_add_mediaplayer_mp4(self, mock_add_mediaplayer_mp4):
        news = open('listanimal/test/html_file_test/news_mp4.html').read()
        soup_url_new = bs(news, 'html.parser')
        time_post = soup_url_new.find('time', 'date')['datetime']
        optimal_date = time_post.split('-')[0] + '.' + time_post.split('-')[1]
        mediaplayer_mp4 = soup_url_new.find('div', 'mediaplayer')
        if mediaplayer_mp4 is not None:
            url_media = mediaplayer_mp4.find('div').attrs['id']
            kod_video = url_media.split('-')[-1]
            url_media_new = 'https://cdnv.rt.com/russian/video/' + \
                            optimal_date + "/" + kod_video + '.mp4'
        mock_add_mediaplayer_mp4.return_value = url_media_new
        result = self.parser.add_mediaplayer_mp4()
        self.assertEqual(result, url_media_new)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.add_mediaplayer_you_tube')
    def test_add_mediaplayer_you_tube(self,mock_add_mediaplayer_you_tube):
        url_media = 'https://www.youtube.com/'
        mock_add_mediaplayer_you_tube.return_value = url_media
        result = self.parser.add_mediaplayer_you_tube()
        self.assertEqual(result, url_media)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.add_galery_media')
    def test_add_galery_media(self, mock_add_galery_media):
        news = open('listanimal/test/html_file_test/news_gallery_img.html').read()
        soup_url_new = bs(news, 'html.parser')
        galery_media = soup_url_new.find_all('div', 'slide')
        summ_gallery = []
        for gallery in galery_media:
            summ_gallery += {str(gallery['data-src'] + ' ')}
        mock_add_galery_media.return_value = summ_gallery
        result = self.parser.add_galery_media()
        self.assertEqual(result, summ_gallery)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.add_news_different_format')
    def test_add_news_different_format(self, mock_add_news_different_format):
        base_url = 'https://russian.rt.com'
        news = open('listanimal/test/html_file_test/news_diff_format.html').read()
        soup = bs(news, 'html.parser')
        all_list_news = soup.find_all('div', 'card__heading_all-new')
        novosti = []
        for list_news in all_list_news:
            url_news = list_news('a', 'link_color')
            for url_new in url_news:
                url_new = base_url + url_new['href']
                soup_usr_new = bs(news, 'html.parser')
                image = soup_usr_new.find('div', 'main-cover')['style']
                first_char = image.find('(') + 1
                last_char = image.rfind(')')
                url_image = image[first_char:last_char]
                time_post = list_news.parent.find('time', 'date')['datetime']
                description_news = soup_usr_new.find('h1', 'main-page-heading__title').text
                all_text = soup_usr_new.find('div', 'page-content')
                heading = all_text.find_all('p')[0].text
                main_text = all_text.find_all('p')[1:]
                full_text = ''
                for parth_text in main_text:
                    full_text += parth_text.text
                set_news = {'url_news': url_new,
                            'description_news': description_news,
                            'heading': heading,
                            'main_text': full_text,
                            'time_post': time_post,
                            'url_media': url_image}
                novosti.append(set_news)
        mock_add_news_different_format.return_value = novosti
        result = self.parser.add_news_different_format()
        self.assertEqual(result, novosti)

class MockTestCreateAnimal(TestCase):
    animal_create = Command()

    @patch('listanimal.management.commands.createanimal.Command.create_animal_objects')
    def test_create_animal_objects(self, mock_create_animal_objects):
        animal_objects = {'animal_type': 'Cat',
            'color': 'Black',
            'age': 'Yong',
            'gender': 'Boy',
            'size': 'Small',
            'photos': 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/49957016/2/?bust=1607082504,'
                      'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/49957016/1/?bust=1607082496,'
                      'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/49957016/3/?bust=1607082505,'
                      'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/49957016/4/?bust=1607082514',
                      'name': 'Piti',
                      'status': 'adoptable'}
        mock_create_animal_objects.return_value = animal_objects
        result = self.animal_create.create_animal_objects()
        self.assertEqual(animal_objects,result)