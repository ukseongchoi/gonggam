import time
import os

from gtts import gTTS
file_name = 'speech.mp3'

import speech_recognition as sr

import pygame

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
        
        sp = gTTS(
            lang='ko',
            text='안녕하세요',
            slow=False
            )
        sp.save(file_name)

        
        pygame.mixer.init()
        tts = pygame.mixer.Sound(file_name)
        tts.play()

        os.remove(file_name)

    except Exception as e:
            print("Exception: " + str(e))



