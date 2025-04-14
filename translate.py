from deep_translator import GoogleTranslator

def translate(frase):
    try:
        traducao = GoogleTranslator(source='en', target='pt').translate(frase)
        return traducao
    except Exception:
        return "Não foi possível traduzir."