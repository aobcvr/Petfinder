from unittest.mock import patch
from unittest import TestCase
from listanimal.parseranimal import RtNewsAnimalParser
from listanimal.management.commands.createanimal import Command


class MockTestParserAnimal(TestCase):
    parser = RtNewsAnimalParser()

    @patch('listanimal.parseranimal.RtNewsAnimalParser.start_parser')
    def test_parser_rt_news(self, mock_rt_news_animal):
        list_news = open('listanimal/test/html_file_test/list_news.html','r').read()
        mock_rt_news_animal.return_value = list_news
        result = self.parser.rt_news_animal()
        self.assertEqual(result, list_news)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.start_parser')
    def test_add_main_text(self, mock_rt_news_animal):
        news = open('listanimal/test/html_file_test/news.html', 'r').read()
        mock_rt_news_animal.return_value = news
        result = self.parser.add_main_text(self, news)
        self.assertEqual(result, news)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.start_parser')
    def test_add_url_media(self, mock_rt_news_animal):
        soup_url_new = open('listanimal/test/html_file_test/url_media.html', 'r').read()
        mock_rt_news_animal.return_value = soup_url_new
        set_news = {}
        result = self.parser.add_url_media(self, set_news, soup_url_new)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.start_parser')
    def test_add_mediaplayer_mp4(self, mock_rt_news_animal):
        news = open('listanimal/test/html_file_test/news_mp4.html').read()
        mock_rt_news_animal.return_value = news
        result = self.parser.add_mediaplayer_mp4(self, news)
        self.assertEqual(result, news)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.start_parser')
    def test_add_galery_media(self, mock_rt_news_animal):
        news = open('listanimal/test/html_file_test/news_gallery_img.html').read()
        mock_rt_news_animal.return_value = news
        result = self.parser.add_galery_media(self, news)
        self.assertEqual(result, news)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.start_parser')
    def test_add_news_different_format(self, mock_rt_news_animal):
        soup_usr_new = open('listanimal/test/html_file_test/news_diff_format.html').read()
        mock_rt_news_animal.return_value = soup_usr_new
        result = self.parser.add_news_different_format(soup_usr_new, list_news, novosti, url_new)

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