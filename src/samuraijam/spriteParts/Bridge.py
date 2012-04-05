'''
Created on Apr 4, 2012

@author: Matt Halpern
'''

import pygame
from samuraijam.util import *

class Bridge(pygame.sprite.Sprite):
    


    def __init__(self, xPos, yPos):
        
        pygame.sprite.Sprite.__init__(self) 
        #self.image, self.rect = load_image('pinkcreep.png',-1)
        
        self.image, self.rect = load_image('bridge.png',-1)
        #self.rect = self.image.get_rect()
        
        self.rect.topleft = (xPos,yPos)
        
    def update(self, dist):
        #self.newX = self.newX - 1
        #self.rect.topleft = (self.newX,self.rect.y)
        self.rect.move_ip(-dist,0)