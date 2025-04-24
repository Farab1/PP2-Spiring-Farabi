import pygame
from datetime import datetime
import os

pygame.init()
w=800
h=800
screen = pygame.display.set_mode((w,h))
fps=60

clock = pygame.time.Clock()

clock = pygame.image.load("clock.png")
minute_hand = pygame.image.load("min_hand.png")
second_hand = pygame.image.load("sec_hand.png")

clock = pygame.transform.scale(clock, (w, h))

def draw_hand(image, angle, length_offset):
    rotated_image = pygame.transform.rotate(image, -angle)
    rect = rotated_image.get_rect()
    rect.center = (w/2, h/2)
    rect.centery -= length_offset
    screen.blit(rotated_image, rect.topleft)

done = True    
while done :
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = False
                        
        now = datetime.now()
        minute = now.minute
        second = now.second

        screen.fill((255, 255, 255))

        screen.blit(clock, (0, 0))

        minute_angle = minute * 6 
        second_angle = second * 6  

        draw_hand(minute_hand, minute_angle, 0)  
        draw_hand(second_hand, second_angle, 0) 

        pygame.display.flip()

        pygame.time.Clock().tick(fps)

pygame.quit()
