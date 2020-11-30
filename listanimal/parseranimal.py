from bs4 import BeautifulSoup as bs
import requests


class RtNewsAnimalParser:

    def rt_news_animal(self):
        """
        Эта функция парсит https://russian.rt.com/tag/zhivotnye
        all_list_news = последние 15 новостей
        url_new = ссылка на конкретную новость
        heading= заголовок статьи
        time_post = время публикации статьи
        description_news= краткое описание статьи , которое находится
        как в статье ,так и в ее кратном описании на общей странице статей
        """
        headers = {'Accept': '*/*',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; '
                   'Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}
        base_url = 'https://russian.rt.com'
        tag_zhivotnie = base_url + '/tag/zhivotnye'
        session = requests.Session()
        request = session.get(tag_zhivotnie, headers=headers)
        soup = bs(request.content, 'html.parser')
        all_list_news = soup.find_all('div', 'card__heading_all-new')
        novosti = []
        for list_news in all_list_news:
            url_news = list_news('a', 'link_color')
            for url_new in url_news:
                url_new = base_url + url_new['href']
                request_url_new = session.get(url_new, headers=headers)
                soup_url_new = bs(request_url_new.content, 'html.parser')
                heading = soup_url_new.find('div', 'article__summary').text
                time_post = soup_url_new.find('time', 'date')['datetime']
                set_news = {'url_news': url_new,
                            'description_news': list_news.text.strip(),
                            'heading': heading.strip(),
                            'time_post': time_post}
                RtNewsAnimalParser.add_main_text(set_news, soup_url_new)
                RtNewsAnimalParser.add_url_media(set_news, soup_url_new)
                RtNewsAnimalParser.add_mediaplayer_mp4(set_news,
                                                       time_post, soup_url_new)
                RtNewsAnimalParser.add_mediaplayer_you_tube(soup_url_new,
                                                            set_news)
                RtNewsAnimalParser.add_galery_media(soup_url_new, set_news)
                novosti.append(set_news)
        return novosti

    def add_main_text(set_news, soup_url_new):
        """
        main_text= основной текст находящийся на странице статьи
        """
        main_text = soup_url_new.find('div', 'article__text')
        if main_text is not None:
            main_text_find_all = main_text.find_all('p')
            full_text = ''
            for main_text_p in main_text_find_all:
                full_text += main_text_p.text
            set_news.update({'main_text': full_text})

    def add_url_media(set_news, soup_url_new):
        """
        url_media= принимает в значение картинки, видео
        (может быть как mp4 так и с youtube)
        """
        url_media = soup_url_new.find('img', 'article__cover-image')
        if url_media is not None:
            set_news.update({'url_media': url_media['src']})

    def add_mediaplayer_mp4(set_news, time_post, soup_url_new):
        """
        url_media = видео(mp4)
        """
        optimal_date = time_post.split('-')[0] + '.' + time_post.split('-')[1]
        mediaplayer_mp4 = soup_url_new.find('div', 'mediaplayer')
        if mediaplayer_mp4 is not None:
            url_media = mediaplayer_mp4.find('div').attrs['id']
            kod_video = url_media.split('-')[-1]
            url_media_new = 'https://cdnv.rt.com/russian/video/' + \
                            optimal_date + "/" + kod_video + '.mp4'
            set_news.update({'url_media': url_media_new})

    def add_mediaplayer_you_tube(soup_url_new, set_news):
        """
        url_media = видео(youtube)
        """
        mediaplayer_you_tube = soup_url_new.find_all('div', 'slide')
        if mediaplayer_you_tube is []:
            url_media = soup_url_new.find('iframe', 'cover__video')
            if url_media is not None:
                you_tube_url = 'https:' + url_media['src']
                set_news.update({'url_media': you_tube_url})

    def add_galery_media(soup_url_new, set_news):
        """
        galery_media = при наличии в статье нескольких фотографий,
        вместо url_media принимаются все фотографии в galery_media
        """
        galery_media = soup_url_new.find_all('div', 'slide')
        summ_gallery = []
        for gallery in galery_media:
            summ_gallery += {str(gallery['data-src'] + ' ')}
        set_news.update({'gallery_img': summ_gallery})
