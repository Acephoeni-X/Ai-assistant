import pyttsx3
import datetime
import speech_recognition as sr
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate=170
engine.setProperty('rate',newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    speak("Welcome master!")
    speak("This is Tokyo your AI assistant")
    # speak("Today's date is")
    
    # year=int(datetime.datetime.now().year)
    # month=int(datetime.datetime.now().month)
    # date=int(datetime.datetime.now().day)
    # speak(date)
    # speak(month)
    # speak(year)
    # speak("The current time in my watch is")

    # Time=datetime.datetime.now().strftime("%H:%M:%S")
    # speak(Time)
    
    hour=int(datetime.datetime.now().hour)
    if hour>=6 and hour<=12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon sir!")
    elif hour>=18 and hour<=24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")   

    speak("I am at your service. How may i help you?")               
wishme()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print(query)
        speak(query)
    except Exception as e:
        print(e)
        speak("Please repeat that one more time...")
        return"None"
    return query
takecommand()
if __name__=="__main__":
    wishme()
    takecommand()




















