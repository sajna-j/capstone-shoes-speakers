from gtts import gTTS
import os


text = "Hello Jasmine"
tts = gTTS(text=text, lang='en')
tts.save("hello.mp3")
os.system("mpg321 hello.mp3")  # You'll need to install mpg321 or use another audio player
