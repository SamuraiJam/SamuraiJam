'''
Created on Apr 23, 2012

@author: jaywaldron
'''
import os, sys
import pygame
from samuraijam.util.Helpers import *

class Healthpack(pygame.sprite.Sprite):
    '''
    classdocs
    '''


    def __init__(self, xPos, yPos):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self) 
        #self.image, self.rect = load_image('pinkcreep.png',-1)
        
        self.image, self.rect = load_image_from_folder('powerups', 'health_pack.png',-1)
        #self.rect = self.image.get_rect()
        
        self.rect.topleft = (xPos,yPos)
        
        self.hit_once = False

    def update(self, dist):
        #self.newX = self.newX - 1
        #self.rect.topleft = (self.newX,self.rect.y)
        self.rect.move_ip(-dist,0)
    
        