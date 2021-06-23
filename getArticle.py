#news api
    #api key: 33d4079bbea841fcaf722a3206624a35
    #https://newsapi.org/ 
    #https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=API_KEY
from testText import *
import requests
from datetime import datetime, timedelta


def get_articles(topic, to):
    #set query for the topic
    q = "&q="+ topic
    #Finds date from one week ago to use as start date for search
    today = datetime.today()
    start_date = today-timedelta(days = 7)
    start_date_string = "from = "+start_date.strftime("%m/%d/%Y")
    #key to get access to api
    api_key = '33d4079bbea841fcaf722a3206624a35'

    #call GET request with api url
    articles = requests.get('https://newsapi.org/v2/everything?'+start_date_string+q+'&apiKey='+api_key)
    articles_json = articles.json()
    #create body to send in email
    body = ''
    #extract urls of each article and add them to the body
    for art in articles_json['articles']: 
        body = body + '\n\n' +art['url']
    #send email with body
    email_alert(topic, body, to)

if __name__ == '__main__':
        topic = input("Enter Topic to Search: ")
        get_articles(topic, "cgalexy1@gmail.com")
        #get_articles(topic, "2672709152@vtext.com") 