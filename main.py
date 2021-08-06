import datetime
import os
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import geocoder


chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please Tell me how i may help you")
def takeCommand():
    #It takes microphone input from the User and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        print(f"User said: {query}\n")
        
    except Exception as e:
        #print(e)
        print("Say That again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")

        elif "play music" in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, The Time is {strTime}")
        elif "open whatsapp" in query:
            wappath = "C:\\Users\\timre\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(wappath)
        elif "where am i" in query:
            g = geocoder.ip('me')
            myLocation = g.city
            print("Your Current Location is:", g.city)
            speak(f"Your Current Location is: {g.city}")





