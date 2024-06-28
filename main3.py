from gtts import gTTS
from playsound import playsound 
txt = '안녕하세요.'
tts = gTTS(text = txt, lang = 'ko')
tts.save("hi.mp3")
playsound("hi.mp3")