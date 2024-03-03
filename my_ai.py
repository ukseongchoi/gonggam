from gtts import gTTS

audio = 'speech.mp3'
language = 'ko'

sp = gTTS(
    lang=language,
    text="공감수학학원",
    slow=False
)
sp.save(audio)



import speech_recognition
import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, timeout = 5, phrase_time_limit = 5)

try:
    result = r.recognize_google(audio, language = "ko-KR")
    print(result)
except speech_recognition.UnknownValueError:
    print("음성 인식 실패")
except speech_recognition.RequestError:
    print("HTTP Request Error 발생")
except speech_recognition.WaitTimeoutError:
    print("WaitTimeout Error 발생 ㅠㅠ")
