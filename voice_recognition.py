import pyttsx3 as p
import speech_recognition as sr
engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',200)
print(rate)
engine.say("hello world")
engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()

speak("hello sir iam a voice assistant")
speak("i hope you are fine")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
        speak("iam having a good day sir")
speak("what can i do for you")
