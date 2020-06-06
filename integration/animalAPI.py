import requests
token=[]
f = open('/home/gil/Рабочий стол/work2/petfinder/listanimal/TextAnimal/ListAnimal.txt','w')
def List_Animal():
    url = 'https://api.petfinder.com/v2/oauth2/token'
    UrlRequestAnimal='https://api.petfinder.com/v2/animals'
    client_id = '4kmEPoUx7DouJMRaJN9QHu5EcM1dVQTUgDbwRnqEEBtXuRfb2u'
    client_secret = 'hGgbY89V0oa6L0IkbXvYWObwfyisDAVaYAPiIkYg'
    grant_type = 'client_credentials'
    request_token = requests.post(url, data={'client_id':client_id,'client_secret':client_secret,'grant_type':grant_type})
    token.append(str(request_token.text.split('"')[9]))
    request_animal=requests.get(UrlRequestAnimal, headers={'Authorization':'Bearer'+' '+token[0]})
    f.write(request_animal.text)
    f.close()
List_Animal()
