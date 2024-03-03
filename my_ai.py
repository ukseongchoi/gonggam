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


while True:

    try:
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout = 5, phrase_time_limit = 5)

        result = r.recognize_google(audio, language = "ko-KR")
        stt += result
        print(stt)
        

    except Exception as e:
            print("Exception: " + str(e))



