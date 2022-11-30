import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
wiki = wikipedia

def talk(text):
 engine.say(text)
 engine.runAndWait()


def talk_command():
    try:
        with sr.Microphone() as source:
           talk("Listening")
           print("Listening...")
           voice = listener.listen(source)
           command = listener.recognize_google(voice)
           command = command.lower()
           if "air" in command:
               command = command.replace('air', '')
               print(command)  
               engine.say(command)
               engine.runAndWait()
               
        

    except: 
        pass
    return command

def run_air():
    command = talk_command()
    print(command)
    if 'play' in command:
        Song = command.replace('play', '')
        talk('playing' + Song)
        pywhatkit.playonyt(Song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("Current time is: " + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wiki.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        jokes = talk(pyjokes.get_joke())
        print(jokes)
    else:
        talk("I coudn't understand you.please say it again")    
while True:
  run_air()        