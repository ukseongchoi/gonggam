import time
import os

from gtts import gTTS
file_name = 'speech.mp3'

import speech_recognition as sr

import pygame
pygame.mixer.init()

stt = ''

while True:
    try:
         
        r = sr.Recognizen(source, timeout = 5, phrase_time_limit = 5)

        result = r.recognize_google(audio, language = "ko-KR")
        stt += result
        print(stt)

        sp = gTTS(
            lang='ko',
            text=result,
            slow=False
            )
        sp.save(file_name)

        tts = pygame.mixer.Sound(file_name)
        tts.play()

        os.remove(file_name)

    except Exception as e:
            print("Exception: " + str(e))



