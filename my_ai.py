import time
import os

from gtts import gTTS

import speech_recognition as sr

audio = 'speech.mp3'

import pygame
pygame.mixer.init()

stt = ''

while True:

    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout = 5, phrase_time_limit = 5)

    try:
        result = r.recognize_google(audio, language = "ko-KR")
        stt += result
        print(stt)

        sp = gTTS(
            lang='ko',
            text=result,
            slow=False
            )
        sp.save(audio)

        tts = pygame.mixer.Sound('speech.mp3')
        tts.play()

        os.remove(audio)
        
    except Exception as e:
            print("Exception: " + str(e))



