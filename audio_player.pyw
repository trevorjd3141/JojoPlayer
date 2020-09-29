# Press F6 to start music

import pygame
import time
import os

pygame.mixer.init()
print(os.getcwd())
pygame.mixer.music.load("T:\Coding Projects\Jojo_Music\\new_giogio_theme.mp3")
pygame.mixer.music.play(start=160.5)

curr_volume = 0.0
pygame.mixer.music.set_volume(curr_volume)
while pygame.mixer.music.get_pos() < 3*1000:
    curr_volume += 0.0000003
    pygame.mixer.music.set_volume(curr_volume)

time.sleep(27)

while pygame.mixer.music.get_volume() > 0.0:
    curr_volume -= 0.000000125
    pygame.mixer.music.set_volume(curr_volume)

pygame.mixer.music.stop()
