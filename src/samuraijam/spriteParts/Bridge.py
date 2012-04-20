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
        bridge_num = (yPos-39)/72
        bridges = {0 : 'green_bridge.png', 1 : 'red_bridge.png', 2 : 'yellow_bridge.png', 3 : 'blue_bridge.png', 4 : 'orange_bridge.png'}

        self.image, self.rect = load_image(bridges[bridge_num],-1)
        #self.rect = self.image.get_rect()
        
        self.rect.topleft = (xPos,yPos)
        
    def update(self, dist):
        #self.newX = self.newX - 1
        #self.rect.topleft = (self.newX,self.rect.y)
        self.rect.move_ip(-dist,0)