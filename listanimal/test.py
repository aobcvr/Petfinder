from unittest.mock import patch
from unittest import TestCase, main
from listanimal.parseranimal import RtNewsAnimalParser
class MockTestListanimal(TestCase):
    parser = RtNewsAnimalParser()

    @patch('listanimal.parseranimal.RtNewsAnimalParser.rt_news_animal')
    def test_parser_rt_news(self,mock_rt_news_animal):
        novosti = [
            {'url_news': 'https://russian.rt.com/russia/news/808915-mts-moskovskii-zoopark-deti-ekologiya',
             'description_news': 'Компания МТС и Московский зоопарк '
                                 'запустили творческо-образовательную '
                                 'программу по экологии для школьников'
                                 ' в рамках федерального благотворительного '
                                 'проекта «Поколение М». ',
             'heading': 'МТС и Московский зоопарк запустили онлайн-программу по экологии для школьников',
             'time_post': '2020-12-2 15:50'}]
        mock_rt_news_animal.return_value = novosti
        result = self.parser.rt_news_animal()
        self.assertEqual(result, novosti)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.add_main_text')
    def test_add_main_text(self, mock_add_main_text):
        main_text = 'По мнению международной группы климатологов ' \
                    'из Республики Корея, Китая, Швеции, США'
        mock_add_main_text.return_value = main_text
        result = self.parser.add_main_text()
        self.assertEqual(result, main_text)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.add_url_media')
    def test_add_url_media(self, mock_add_url_media):
        url_media = 'https://cdni.rt.com/russian/images/2020.11/article/5fbe67abae5ac910bb65c4b4.jpg'
        mock_add_url_media.return_value = url_media
        result = self.parser.add_url_media()
        self.assertEqual(result, url_media)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.add_mediaplayer_mp4')
    def test_add_mediaplayer_mp4(self, mock_add_mediaplayer_mp4):
        url_media = 'https://cdnv.rt.com/russian/video/2020.12/5fca3d7a02e8bd38d3213228.mp4'
        mock_add_mediaplayer_mp4.return_value = url_media
        result = self.parser.add_mediaplayer_mp4()
        self.assertEqual(result, url_media)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.add_mediaplayer_you_tube')
    def test_add_mediaplayer_you_tube(self,mock_add_mediaplayer_you_tube):
        url_media = 'https://www.youtube.com/'
        mock_add_mediaplayer_you_tube.return_value = url_media
        result = self.parser.add_mediaplayer_you_tube()
        self.assertEqual(result, url_media)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.add_galery_media')
    def test_add_galery_media(self, mock_add_galery_media):
        gallery_img = 'https://cdni.rt.com/russian/images/2020.11/original/5fbcfaa8ae5ac94e3b330393.jpg ,' \
                      'https://cdni.rt.com/russian/images/2020.11/original/5fba499302e8bd25af1c878a.jpg ,' \
                      'https://cdni.rt.com/russian/images/2020.11/original/5fba4743ae5ac940cc4ed737.jpg ,' \
                      'https://cdni.rt.com/russian/images/2020.11/original/5fba4742ae5ac940cc4ed736.jpg ,'
        mock_add_galery_media.return_value = gallery_img
        result = self.parser.add_galery_media()
        self.assertEqual(result, gallery_img)

    @patch('listanimal.parseranimal.RtNewsAnimalParser.add_news_different_format')
    def test_add_news_different_format(self, mock_add_news_different_format):
        novosti = [
            {'url_news': 'https://russian.rt.com/russia/article/808880-rebyonok-opeka-dom-podzhog',
             'description_news': 'В Нижнем Новгороде органы опеки через '
                                 'суд добиваются изъятия из семьи',
             'heading': '«Необоснованные проверки»: в Нижнем Новгороде '
                        'опека хочет забрать ребёнка из семьи, которая '
                        'столкнулась с травлей',
             'time_post': '2020-12-2 19:16'}]
        mock_add_news_different_format.return_value = novosti
        result = self.parser.add_news_different_format()
        self.assertEqual(result, novosti)