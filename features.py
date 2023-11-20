#use pocketspnix for pdf tings
#has the features language detection, text to speech, speech to text, pdf to text
from gtts import gTTS
import speech_recognition as sr
import pygame # for audio playback
import fitz  # PyMuPDF
from langid import classify # for multiple langs not using here show example of one them tamil pls
def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")#maybe problemv where it'll save the file in the same directory as the code
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
#here fro windows so 
#file_path = r'C:\Users\91951\OneDrive\Desktop\MPMCs\nameoffile.pdf'
#pdf_to_text(file_path) to convert obviously
text_input = "Hello, how are you?"
language_input = 'en'  # Choose from 'en', 'hi', 'ta', 'te', 'kn' 
#this part is to be recognized or not ? 
text_to_speech(text_input, language=language_input)
text = speech_to_text(language=language_input)
# For PDF-to-text
pdf_path = r'C:\\Users\\91951\\OneDrive\Desktop\\MPMCs\\devsfile.pdf'  # Replace with your PDF file path
pdf_text = pdf_to_text(pdf_path)
print(pdf_text)
#more to add are like if someone wants the bot to read all the stuff inpdf in a simplified text 