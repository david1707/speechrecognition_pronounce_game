import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    mic_data = r.listen(source)
    text_data = r.recognize_google(mic_data)
    print(text_data)
    