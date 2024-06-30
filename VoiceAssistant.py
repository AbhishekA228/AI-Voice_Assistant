import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener=sr.Recognizer()
engine=pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'Vijay' in command:
                command=command.replace('Vijay','')
                print(command)
    except:
        pass
    return command
def run_vijay():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        print('Playing '+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)
    elif 'tell me about' in command:
        person=command.replace('tell me about','')
        info=wikipedia.summary(person,1)
        print(person+':')
        print(info)
        print()
        talk(info)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)
        print(person+':')
        print(info)
        print()
        talk(info)
    elif 'can i know about' in command:
        person=command.replace('can i know about','')
        info=wikipedia.summary(person,1)
        print(person+':')
        print(info)
        print()
        talk(info)
    elif 'are you single' in command:
        talk('No i am committed to my work')
        print('No i am committed to my work')
    elif 'joke' in command:
        x=pyjokes.get_joke()
        print(x)
        talk(x)
    elif 'quit' in command:
        exit()
    else:
        talk('Please say the command again.')
        print('Please say the command again.')
while True:
    run_vijay()