from modules.AN_googletrans import *

if __name__ == "__main__":
    # Example usage
    text = "こんにちは"
    
    translatedText = translate_text_auto(text)
    print(f"Translated to Japanese: {translatedText}")

    # Translating back to English
    translatedText = translate_text_auto(translatedText)
    print(f"Translated back to English: {translatedText}")