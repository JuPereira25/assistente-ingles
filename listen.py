import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale algo em inglês:")
        recognizer.pause_threshold = 2
        audio = recognizer.listen(source)
    try:
        phrase = recognizer.recognize_google(audio, language='en-us')
        return phrase.lower()
    except Exception:
        print("Não entendi.")
        return ""