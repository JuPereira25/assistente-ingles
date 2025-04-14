import speech_recognition as sr 
import pyttsx3
import time
from deep_translator import GoogleTranslator


engine = pyttsx3.init("sapi5")
engine.setProperty('voice', engine.getProperty("voices")[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale algo em inglês:")
        recognizer.pause_threshold = 2
        audio = recognizer.listen(source)
    try:
        frase = recognizer.recognize_google(audio, language='en-us')
        print("Você disse:" + frase + "\n")
        return frase.lower()
    except Exception as e:
        print("Não entendi.")
        return ""

def translate(frase):
    try:
        traducao = GoogleTranslator(source='en', target='pt').translate(frase)
        return traducao
    except Exception as e:
        return "Não foi possível traduzir."

# Loop principal
if __name__ == "__main__":
    speak("Olá! Pode começar a falar.")
    while True:
        frase_ouvida = listen()
        if frase_ouvida:
            print("Você disse (inglês):", frase_ouvida)

            if "bye" in frase_ouvida:
                speak("Bye bye! Encerrando o programa.")
                break

            traducao = translate(frase_ouvida)
            print("Tradução (português):", traducao)

            speak("Você disse: " + frase_ouvida)
            speak("A tradução é: " + traducao)





