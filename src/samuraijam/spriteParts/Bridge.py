'''
Created on Apr 4, 2012

@author: Matt Halpern
'''

import pygame
from samuraijam.util import *

class Bridge(pygame.sprite.Sprite):
    
    BRIDGE_TYPE_GREEN = 'green_bridge.png'
    BRIDGE_TYPE_RED = 'red_bridge.png'
    BRIDGE_TYPE_YELLOW = 'yellow_bridge.png'
    BRIDGE_TYPE_BLUE = 'blue_bridge.png'
    BRIDGE_TYPE_ORANGE = 'orange_bridge.png'
    
    def __init__(self, xPos, yPos):
        
        pygame.sprite.Sprite.__init__(self) 
        bridge_num = (yPos-39)/72
        bridges = {0 : self.BRIDGE_TYPE_GREEN, 1 : self.BRIDGE_TYPE_RED, 2 : self.BRIDGE_TYPE_YELLOW, 3 : self.BRIDGE_TYPE_BLUE, 4 : self.BRIDGE_TYPE_ORANGE}
        self.bridge_type = bridges[bridge_num]
        self.image, self.rect = load_image_from_folder('bridges', bridges[bridge_num], -1)
        
        self.rect.topleft = (xPos,yPos)
        
    def update(self, dist):
        self.rect.move_ip(-dist,0)