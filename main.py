import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
apiKey = "d007c733cfb042f995726f7508481f18"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1] +" "+ c.lower().split(" ")[2]
        print(song)
        webbrowser.open(musicLibrary.music[song])
    elif "news" in c.lower():
        print("in news")
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={apiKey}")

            news_data = r.json()  # Convert response to JSON format
    
            # Check if articles are present
            if 'articles' in news_data:
                for i in range(4)
                    for article in news_data['articles']:
                        print("in article")
                        speak(f"{article['title']}")

            else:
                speak("No articles found.")
        except requests.exceptions.RequestException as e:
            speak(f"Error fetching news: {e}")
    else:
        print("Something wrong")



if __name__ == "__main__":
    speak("Initiating Jarivis>>")
    # Listen for the wake word Jarvis
    while True:
        r = sr.Recognizer()
        
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)

            word = r.recognize_google(audio)
            print(word)
            if (word.lower()=="jarvis"):
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Acitve...")
                    audio = r.listen(source)
                command = r.recognize_google(audio)

                processCommand(command)
                
            
        except Exception as e:
            print(e)
         
    
    