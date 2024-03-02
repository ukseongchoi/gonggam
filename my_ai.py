from gtts import gTTS

audio = 'speech.mp3'
language = 'ko'

sp = gTTS(
    lang=language,
    text="공감수학학원",
    slow=False
)
sp.save(audio)
