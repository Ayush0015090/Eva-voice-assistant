import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak (text):
    engine.say(text)
    engine.runAndWait()
newsapi = "f5e5efb2103b4964b7429f3b450b797d"


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com") 
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        if song in musiclibrary.music:
            link = musiclibrary.music[song]
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}")

    elif "news" in c.lower():
        try:
            r = requests.get(f"https://newsapi.org/v2/everything?q=headlines&language=en&apiKey={newsapi}")

            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
            # Print the headlines
                if articles:
                    for article in articles[:5]:
                        speak(article['title'])
                else:
                    speak("no news articles found")  
        except Exception as e:
            print(f"News Error: {e}")
            speak("Sorry, there was an error fetching the news.")          

    else:
        pass

    


if __name__ == "__main__":
    speak("Initializing eva....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=4)
            word = r.recognize_google(audio)
            if(word.lower() == "eva"):
                speak("yes")
                # Listen for command
                with sr.Microphone() as source:
                    print("eva Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))