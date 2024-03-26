import sys
from googletrans import Translator, LANGUAGES
import configparser

def get_dest(src):
    """
    get destinated language from source language based on user config
    
    :param src: the language of the source text
    :param config_file: Path to the .ini configuration file.
    :return: target destinated language of source language
    """
    config = configparser.ConfigParser()
    config.read("config.ini")
    languages = config['DEFAULT']['Languages']
    if src in languages:
        dest = config[src]['DestLanguage']
    else:
        dest = src
    return dest

def translate_text_auto(text):
    """
    Translate text from source language to destination language.

    :param text: The text to translate.
    :param src: Source language (default is English).
    :param dest: Destination language (default is Japanese).
    :return: Translated text.
    """
    translator = Translator()
    # auto language detection
    detect = translator.detect(text)
    src = detect.lang
    print(f"detected language: {src}")
    dest = get_dest(src)
    outputText = ""
    if (src == dest):
        outputText = (f"unconfigured language, detected language: {dest}")
    else:
        try:
            translation = translator.translate(text, src=src, dest=dest)
            outputText = translation.text
        except Exception as e:
            print(f"found text is: {text}")
            #outputText = (f"An error occurred: {e}")
            return False
    return outputText