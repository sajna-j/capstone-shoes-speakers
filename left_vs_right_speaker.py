# Create Sound and Channel instances.
"""
sound0 = pg.mixer.Sound('redbone.wav')
channel0 = pg.mixer.Channel(0)

# Play the sound (that will reset the volume to the default).
channel0.play(sound0)
# Now change the volume of the specific speakers.
# The first argument is the volume of the left speaker and
# the second argument is the volume of the right speaker.
channel0.set_volume(1.0, 0.0)
"""

import pygame
from pygame.locals import *

pygame.init() # init all the modules

sound = pygame.mixer.Sound('redbone.wav') # import the sound file

sound_played = False
# sound has not been played, so calling set_volume() will return an error

screen = pygame.display.set_mode((640, 480)) # make a screen

running = True
while running: # main loop
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN: # play the sound file
            channel = sound.play()
            sound_played = True
            # start setting the volume now, from this moment where channel is defined

    # calculate the pan
    left = 0
    right = 1

    # pan the sound if the sound has been started to play
    if sound_played:
        channel.set_volume(left, right)
