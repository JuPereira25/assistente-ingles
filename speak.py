import pyttsx3

engine = pyttsx3.init("sapi5")
engine.setProperty('voice', engine.getProperty("voices")[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()