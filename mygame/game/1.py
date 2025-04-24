import pygame # type: ignore
import math
import pygame, sys # type: ignore
from pygame.locals import * # type: ignore
import random, time
import pygame.transform # type: ignore

from pygame.sprite import Group 
#Intialization pygame
pygame.init()

#Setting up FPS 
FPS = 15
FramePerSec = pygame.time.Clock()

#Parameters for window
SCREEN_WIDTH, SCREEN_HEIGHT= 1280, 640
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GAME")

#Colors
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)

icon = pygame.image.load(r'C:\Users\Asus\Downloads\unnamed.png')
pygame.display.set_icon(icon)

#pygame.mixer.Sound(r"C:\Users\Asus\Downloads\bccc.wav").play(-1)

bc=pygame.image.load(r"C:\Users\Asus\Downloads\Flat_Game_Background_3..jpg")
bc_x=0
ply = 480
player=pygame.image.load(r'C:\Users\Asus\Downloads\dinoooo.jpg')
player = pygame.transform.scale(player, (100, 100))
plrect = player.get_rect()

running=True
#Game cycle
while running:

    screen.blit(bc, (bc_x,0))
    screen.blit(bc, (bc_x+ 1280,0))
    screen.blit(player, (440,ply))
    
    if bc_x < -1200:
        bc_x=0
    else:
        bc_x -= 60

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]: 
            ply-=150
        if pressed_keys[K_DOWN]:
            ply+=150
            
       
    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()