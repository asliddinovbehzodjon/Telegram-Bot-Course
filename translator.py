from deep_translator import GoogleTranslator
def tarjimon(text):
    tarjima = GoogleTranslator(source='uz',target='en').translate(text)
    return tarjima
