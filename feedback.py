import speech_recognition as sr
from difflib import SequenceMatcher
from speak import speak  

def feedback_pronuncia(texto_esperado):
    recognizer = sr.Recognizer()
    with sr.Microphone() as fonte:
        speak("Repita a frase.")
        recognizer.pause_threshold = 2
        audio = recognizer.listen(fonte)
    
    try:
        texto_ouvido = recognizer.recognize_google(audio, language='en-us')
        
        similaridade = SequenceMatcher(None, texto_esperado.lower(), texto_ouvido.lower()).ratio()
        
        if similaridade > 0.8:
            speak("Boa pronúncia!")
        else:
            speak("A pronúncia pode melhorar.")
    
    except Exception as e:
        speak("Não entendi o que você disse. Tente novamente.")
