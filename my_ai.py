from gtts import gTTS
import speech_recognition as sr

audio = 'speech.mp3'
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout = 5, phrase_time_limit = 5)

stt = ''
while True:

    try:
        result = r.recognize_google(audio, language = "ko-KR")
        stt = result
        print(stt)
    except speech_recognition.UnknownValueError:
        print("음성 인식 실패")
    except speech_recognition.RequestError:
        print("HTTP Request Error")
    except speech_recognition.WaitTimeoutError:
        print("WaitTimeout Error")



sp = gTTS(
    lang='ko',
    text="공감수학학원",
    slow=False
)
sp.save(audio)