#use pocketspnix for pdf tings
#has the features language detection, text to speech, speech to text, pdf to text
from gtts import gTTS
import speech_recognition as sr
import pygame # for audio playback
import fitz  # PyMuPDF
from langid import classify
from googletrans import Translator # for multiple langs not using here show example of one them tamil pls
def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    #maybe problemv where it'll save the file 
    #in the same directory as the code 
    # what if a combination of mulotiple language is spoken ?
def speech_to_text(language='en'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language=language)
        print("You :", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
        return None
def pdf_to_text(pdf_path)->str:
    doc = fitz.open(pdf_path)#replace with your pdf file path
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    return text
def detect_language(text):
    # Language detection using langid
    lang, _ = classify(text)
    return lang
def translate_text(text, target_lang='en'):
    # Google Translate API for translation
    translator = Translator()
    translated_text = translator.translate(text, dest=target_lang)
    return translated_text.text
