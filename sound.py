import pygame
from openai import OpenAI

filename = 's_key.txt'
f = open(filename, 'r')
OPENAI_API_KEY = f

#client = OpenAI(api_key = OPENAI_API_KEY)


pygame.mixer.init()
bang =  pygame.mixer.Sound("t_time")
bang.play()