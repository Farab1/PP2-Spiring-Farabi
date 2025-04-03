'''import pygame
import os

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()
x=20
y=20
screen = pygame.display.set_mode((400, 300))
done = True
clock = pygame.time.Clock()

while  done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((255, 255, 255))
        
        screen.blit(get_image('ball.png'), (x, y))
        
        pygame.display.flip()
        clock.tick(60)'''

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

        minute_angle = minute * 7.5 
        second_angle = second * 6  

        draw_hand(minute_hand, minute_angle, 0)  
        draw_hand(second_hand, second_angle, 0) 

        pygame.display.flip()

        pygame.time.Clock().tick(fps)

pygame.quit()
