import openai

from openai import OpenAI
filename = 's_key.txt'
file = open(filename, 'r')
OPENAI_API_KEY = file.read()
print(OPENAI_API_KEY)

openai.api_key = OPENAI_API_KEY
import time
import os

from gtts import gTTS

import speech_recognition as sr

import pygame


def get_sound(text):
    
    sp = gTTS(
    lang='ko',
    text=text,
    slow=False
    )
    sp.save('stt.mp3')

def get_audio1():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("지금 말씀하세요: ")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = " "

        try:
            said = r.recognize_google(audio, language="ko-KR")
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    
    return said

def get_audio2():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("지금 말씀하세요: ")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = " "

        try:
            said = r.recognize_google(audio, language="ko-KR")
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    
    return said
    
stt = ''
while True:
    print('시작')
    stt += get_audio1()

    if stt.replace(' ','').find('헤이공감') > -1:
        pygame.mixer.init()
        
        tts = pygame.mixer.Sound('yes.mp3')
        tts.play()
        
        time.sleep(2)
        
        recognation_sound = pygame.mixer.Sound('Pling Sound.mp3')
        recognation_sound.play()
        
        text = get_audio2()
        recognation_sound.play()
        
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": "{}".format(text),
                },
            ],
        )
        print(completion.choices[0].message.content)
        get_sound(completion.choices[0].message.content)
        
        tts = pygame.mixer.Sound('stt.mp3')
        tts.play()
        recognation_sound.play()
        
        stt = ''





