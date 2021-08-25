import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("hi")
    apiKey = 'apiKey'
    
    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}")
    news_dict = json.loads(r.text)
    # print(news_dict, "newsdict")
    articles = news_dict['articles']
    speak("let's begin")
    speak("first news")
    for items in articles:
        print(items['title'])
        speak(items['title'])
        speak("next headline")
    speak("thank u")
