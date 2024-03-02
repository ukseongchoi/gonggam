
#from openai import OpenAI



filename = 's_key.txt'
f = open(filename, 'r')
OPENAI_API_KEY = f

#client = OpenAI(api_key = OPENAI_API_KEY)

import pygame
import time
pygame.mixer.init()

bell_t_time =  pygame.mixer.Sound("t_time.mp3")
bell_start = pygame.mixer.Sound("start_bell.mp3")

#bell_start.play()
#bell_t_time.play()

STATUS = 0
while True:
	
	time.sleep(1)
	print(time.localtime().tm_hour)
	print(time.localtime().tm_min)
	print(time.localtime().tm_wday)
	
	now_hour = time.localtime().tm_hour
	now_min = time.localtime().tm_min
	now_today = time.localtime().tm_wday
	if now_today == 5:
		
		print('s')
		if now_hour == 10 and now_min == 00:
			bell_start.play()
			time.sleep(61)
		
		elif now_hour == 11 and now_min == 30:
			bell_start.play()
			time.sleep(61)
		
		elif now_hour == 12 and now_min == 15:
			bell_t_time.play()	
			time.sleep(61)
		
		elif now_hour == 13 and now_min == 00:
			bell_start.play()
			time.sleep(61)
			
		elif now_hour == 13 and now_min == 45:
			bell_t_time.play()
			time.sleep(61)

		elif now_hour == 14 and now_min == 30:
			bell_start.play()
			time.sleep(61)
		
		
	else:
		
		if now_hour == 17 and now_min == 30:
			bell_start.play()
			time.sleep(61)
		
		elif now_hour == 19 and now_min == 00:
			bell_start.play()
			time.sleep(61)
		
		elif now_hour == 19 and now_min == 45:
			bell_t_time.play()	
			time.sleep(61)
		
		elif now_hour == 20 and now_min == 30:
			bell_start.play()
			time.sleep(61)
			
		elif now_hour == 21 and now_min == 15:
			bell_t_time.play()
			time.sleep(61)

		elif now_hour == 22 and now_min == 00:
			bell_start.play()
			time.sleep(61)
