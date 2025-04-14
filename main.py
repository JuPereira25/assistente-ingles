from speak import speak
from listen import listen
from translate import translate
from feedback import feedback_pronuncia

if __name__ == "__main__":
    speak("Olá, Vamos Praticar!.")
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

            feedback_pronuncia(frase_ouvida)

