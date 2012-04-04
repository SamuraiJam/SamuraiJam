import pygame
from pygame.locals import *
from boxes import UpDownBox
from DirtPath import *

pygame.init()
boxes = []
for color, location in [([255, 0, 0], [0, 0]),
                        ([0, 255, 0], [60, 60]),
                        ([0, 0, 255], [120, 120])]:
    boxes.append(UpDownBox(color, location))

paths = []
for location in [[0, 0],[95, 0],[190, 0],
                 [0, 50],[95, 50],[190, 50]
                 ]:
    paths.append(DirtPath(location))

screen = pygame.display.set_mode([500, 500])
while pygame.event.poll().type != KEYDOWN:
    screen.fill([0, 0, 0]) # blank the screen.

    # Save time by only calling this once
    time = pygame.time.get_ticks() 
    '''
    for b in boxes:
        b.update(time, 150)
        screen.blit(b.image, b.rect)
    '''
    for p in paths:
        p.update(time,150)
        screen.blit(p.image, p.rect)
    for b in boxes:
        b.update(time, 150)
        screen.blit(b.image, b.rect)
        

    pygame.display.update()

