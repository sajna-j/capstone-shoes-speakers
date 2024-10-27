from gtts import gTTS
from io import BytesIO
import pygame
from enum import Enum
import subprocess

APPROPRIATE_VOL: int = 30
WAITING_TIME: int = 10  # for playing a single audio to end

class SpeakerChannel(Enum):
    LEFT: int = 1
    RIGHT: int = 2
    BOTH: int = 3

def speak(text, channel: SpeakerChannel=SpeakerChannel.BOTH):
    # this creates speach as a bitstream so we don't need to save an mp3 file anywhere
    mp3_fp = BytesIO()
    tts = gTTS(text=text, lang='en')
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    
    if channel == SpeakerChannel.BOTH:
        set_volume(APPROPRIATE_VOL, APPROPRIATE_VOL)
    elif channel == SpeakerChannel.LEFT:
        set_volume(APPROPRIATE_VOL, 0)
    elif channel == SpeakerChannel.RIGHT:
        set_volume(0, APPROPRIATE_VOL)

    # play audio!
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_fp)
    pygame.mixer.music.play()
    
    # wait for audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(WAITING_TIME)


def set_volume(left_volume, right_volume):
    command = [
        "amixer", 
        "-c", "1",  # specifies card 1
        "sset", 
        "Speaker", 
        f"{left_volume}%,{right_volume}%"
    ]
    
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"Volume set to: Left {left_volume}%, Right {right_volume}%")
    except subprocess.CalledProcessError as e:
        print(f"Error setting volume: {e}")
        print(f"Error output: {e.stderr}")


pygame.init()
speak("Hello! This is the left", SpeakerChannel.LEFT)
speak("Hi! This is the right!", SpeakerChannel.RIGHT)
speak("Goodbye from both speakers!")
