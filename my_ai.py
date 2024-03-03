import time
import os

from gtts import gTTS
file_name = 'speech.mp3'

import speech_recognition as sr

import pygame


sp = gTTS(
    lang='ko',
    text='네 안녕하세요',
    slow=False
    )
sp.save('yes.mp3')

        
#pygame.mixer.init()
#tts = pygame.mixer.Sound(file_name)
#tts.play()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("지금 말씀하세요: ")
        audio = r.listen(source)
        said = " "

        try:
            said = r.recognize_google(audio, language="ko-KR")
            print("말씀하신 내용입니다 : ", said)
        except Exception as e:
            print("Exception: " + str(e))
    
    return said

while True:

    print(get_audio())



