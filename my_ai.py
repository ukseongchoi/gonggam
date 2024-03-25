from openai import OpenAI



filename = 's_key.txt'
f = open(filename, 'r')
OPENAI_API_KEY = f

client = OpenAI(api_key = OPENAI_API_KEY)


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
        audio = r.listen(source, timeout = 10, phrase_time_limit = 3)
        said = " "

        try:
            said = r.recognize_google(audio, language="ko-KR")
            print("말씀하신 내용입니다 : ", said)
        except Exception as e:
            print("Exception: " + str(e))
    
    return said

stt = ''
while True:
    stt += get_audio()

    if stt.replace(' ','').find('헤이공감') > -1:
        pygame.mixer.init()
        tts = pygame.mixer.Sound('yes.mp3')
        tts.play()

        break





