from deep_translator import GoogleTranslator

def translate_text(text, target):
    translated_text = GoogleTranslator(source='auto', target=target).translate(text)
    return translated_text