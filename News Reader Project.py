import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    api_key = input("Enter your API key: ")
    category = input("Categories:\nBusiness\nEntertainment\nHealth\nScience\nSports\nTechnology\nEnter your category which you want: ")
    category = category[0].lower() + category[1:]
    url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={api_key}"
    speak("Today's Top News are.")
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict["articles"]
    for article in arts:
        print(article["title"])
        print(article["url"], "\n")
        speak(article["title"])
    speak("Thanks for Listening. Have a nice day")