from bs4 import BeautifulSoup as bs
import requests
headers={'Accept':'*/*',
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}
base_url='https://russian.rt.com'
tag_zhivotnie=base_url+'/tag/zhivotnye'
session=requests.Session()
class RtNewsAnimalParser:
    def rt_news_animal(self):
            request=session.get(tag_zhivotnie,headers=headers)
            soup=bs(request.content,'html.parser')
            all_list_news=soup.find_all('div','card__heading_all-new')
            novosti = []
            for list_news in all_list_news:
                    url_news = list_news('a','link_color')
                    for url_new in url_news:
                            url_new=base_url+url_new['href']
                            request_url_new=session.get(url_new,headers=headers)
                            soup_url_new=bs(request_url_new.content,'html.parser')
                            heading=soup_url_new.find('div','article__summary').text
                            main_text=soup_url_new.find('div','article__text')
                            if main_text is not None:
                                main_text_find_all=main_text.find_all('p')
                                full_text=''
                                for main_text_p in main_text_find_all:
                                    full_text+=main_text_p.text
                            url_media=soup_url_new.find('img','article__cover-image')
                            time_post=soup_url_new.find('time','date')['datetime']
                            optimal_date=time_post.split('-')[0]+'.'+time_post.split('-')[1]
                            if url_media is not None:
                                if main_text is not None:
                                        novosti.append({'url_news': url_new,
                                                        'description_news': list_news.text.strip(),
                                                        'heading': heading,
                                                        'main_text':full_text,
                                                        'url_media': url_media['src'],
                                                        'time_post':time_post})
                                else:
                                        novosti.append({'url_news':url_new,
                                                        'description_news':list_news.text.strip(),
                                                        'heading':heading.strip(),
                                                        'url_media': url_media,
                                                        'time_post': time_post})
                            elif url_media == None:
                                mediaplayer = soup_url_new.find('div','mediaplayer')
                                if mediaplayer is not None:
                                    url_media = mediaplayer.find('div').attrs['id']
                                    kod_video=url_media.split('-')[-1]
                                    if main_text is not None:
                                        novosti.append({'url_news': url_new,
                                                        'description_news': list_news.text.strip(),
                                                        'heading': heading.strip(),
                                                        'url_media':'https://cdnv.rt.com/russian/video/'+optimal_date+"/"+ kod_video+'.mp4',
                                                        'main_text': full_text,
                                                        'time_post': time_post})
                                    else:
                                        novosti.append({'url_news': url_new,
                                                        'description_news': list_news.text.strip(),
                                                        'heading': heading.strip(),
                                                        'url_media': 'https://cdnv.rt.com/russian/video/' + optimal_date + "/" + kod_video + '.mp4',
                                                        'time_post': time_post})
                                elif mediaplayer == None:
                                    url_media = soup_url_new.find_all('div', 'slide')
                                    if url_media == []:
                                        url_media=soup_url_new.find('iframe','cover__video')
                                        if url_media is not None:
                                            you_tube_url=url_media['src']
                                            if main_text is not None:
                                                novosti.append({'url_news': url_new,
                                                                'description_news': list_news.text.strip(),
                                                                'heading': heading.strip(),
                                                                'url_media': 'https:'+you_tube_url,
                                                                'main_text': full_text,
                                                                'time_post': time_post})
                                            else:
                                                novosti.append({'url_news': url_new,
                                                                'description_news': list_news.text.strip(),
                                                                'heading': heading.strip(),
                                                                'url_media': 'https:' + you_tube_url,
                                                                'time_post': time_post})
                                        else:
                                            if main_text is not None:
                                                novosti.append({'url_news': url_new,
                                                            'description_news': list_news.text.strip(),
                                                            'heading': heading.strip(),
                                                            'main_text': full_text,
                                                            'time_post': time_post})
                                            else:
                                                novosti.append({'url_news': url_new,
                                                                'description_news': list_news.text.strip(),
                                                                'heading': heading.strip(),
                                                                'time_post': time_post})
                                    else:
                                        summ_gallery=[]
                                        for gallery in url_media:
                                            summ_gallery+={str(gallery['data-src']+' ')}
                                            if main_text is not None:
                                                novosti.append({'url_news': url_new,
                                                                'description_news': list_news.text.strip(),
                                                                'heading': heading.strip(),
                                                                'gallery_img': summ_gallery,
                                                                'main_text': full_text,
                                                                'time_post': time_post})
                                            else:
                                                novosti.append({'url_news': url_new,
                                                                'description_news': list_news.text.strip(),
                                                                'heading': heading.strip(),
                                                                'gallery_img': summ_gallery,
                                                                'time_post': time_post})
            return novosti