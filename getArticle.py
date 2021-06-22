#news api
    #api key: 33d4079bbea841fcaf722a3206624a35
    #https://newsapi.org/ 
    #https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=API_KEY
from testText import *
import requests

#takes in topic and turns it into the appropriot query for the api
topic = "Senate"
q = "&q="+ topic
api_key = '33d4079bbea841fcaf722a3206624a35'
articles = requests.get('https://newsapi.org/v2/top-headlines?country=us'+q+'&apiKey='+api_key)
articles_json = articles.json()
body = ''
for art in articles_json['articles']: 
    body = body + '\n' +art['url']
print(body)

email_alert(topic, body, "cgalexy1@gmail.com")