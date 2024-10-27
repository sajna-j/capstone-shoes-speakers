from gtts import gTTS
from io import BytesIO
import pygame

def speak(text, language='en'):
    # this creates speach as a bitstream so we don't need to save an mp3 file anywhere
    mp3_fp = BytesIO()
    tts = gTTS(text=text, lang=language)
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    
    # play audio!
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_fp)
    pygame.mixer.music.play()
    
    # wait for audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

pygame.init()
speak("Hello world!")