import time
import os

from gtts import gTTS
file_name = 'speech.mp3'

import speech_recognition as sr

import pygame




def call_ai():
    stt = ''

    while True:
        if stt.replace(" ",'') == "헤이공감":

            sp = gTTS(
            lang='ko',
            text='네 안녕하세요',
            slow=False
            )
            sp.save(file_name)

            pygame.mixer.init()
            tts = pygame.mixer.Sound(file_name)
            tts.play()

            os.remove(file_name)

            break


        try:
            r = sr.Recognizer()
            mic = sr.Microphone()
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout = 5, phrase_time_limit = 5)

        
            result = r.recognize_google(audio, language = "ko-KR")
            stt += result

        except Exception as e:
            print("Exception: " + str(e))



