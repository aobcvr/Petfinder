from vk_api.longpoll import VkLongPoll,VkEventType
import vk_api
from datetime import datetime
import requests
token='8a1b8b0b7d432054f9239f5b2dfd9cf3bc8863c5abd73007f0122cd5feba3fe2576256a0b24007b59d76e'
vk_session=vk_api.VkApi(token=token)
session_api=vk_session.get_api()
longpoll=VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в:'+ str(datetime.strftime(datetime.now(),'%H:%M:%S')))
            print('Тект сообщения:'+str(event.text))
            print(event.user_id)
            response=event.text.lower()
            if event.from_user and not (event.from_me):
                if response=='дай новость':
                    vk_session.method('messages.send',{'user_id':event.user_id,'message':'alarm','random_id':0})
