import os, sys
import pygame
#from Helpers import *
from pygame.locals import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self, velocity, width, yPos):
        pygame.sprite.Sprite.__init__(self) 
        #self.image, self.rect = load_image('pinkcreep.png',-1)
        
        self.image = pygame.image.load('../data/pinkcreep.png')
        self.rect = self.image.get_rect()
        
        self.newX = width-self.rect.width
        self.rect.topleft = (self.newX,yPos)
        
    def update(self, dist):
        #self.newX = self.newX - 1
        #self.rect.topleft = (self.newX,self.rect.y)
        self.rect.move_ip(-dist,0)