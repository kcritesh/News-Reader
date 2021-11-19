import requests

import json

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)
    
if __name__=='__main__':
    speak("Welcome to News Reader by Ritesh")
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=39f6cdfa3b1049af9d7997b1ac78cbc4')
    response = requests.get(url).text
    news_dict = json.loads(response)
    news = news_dict['articles']
    for article in news:
        speak(article['title'])
        speak("Moving on to Next News")