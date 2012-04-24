'''

Our hero (subclass of Sprite)
will contain references to:
    weapon
    hp
    ki (mp)
    reputation
'''
import os, sys
import pygame
from samuraijam.util.Helpers import *
from pygame.locals import *
from samuraijam.control.HAL import HAL
from samuraijam.spriteParts import Bridge

class Samurai(pygame.sprite.Sprite):
    """A hero is born!"""
    
    def __init__(self, guitarStrings):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('CTS-sprite.gif',-1)
        self.guitarStringPaths = guitarStrings
        self.rect.move_ip(0,guitarStrings[2])
        self.curString = 2
        self.score = 0
    

    def move(self, button, bridge):
        if bridge.bridge_type == Bridge.BRIDGE_TYPE_GREEN and self.curString == 0 and button == HAL.GREEN:
            self.curString = 1
            self.update()
        elif bridge.bridge_type == Bridge.BRIDGE_TYPE_GREEN and self.curString == 1 and button == HAL.GREEN:
            self.curString = 0
            self.update()
        elif bridge.bridge_type == Bridge.BRIDGE_TYPE_RED and self.curString == 1 and button == HAL.RED:
            self.curString = 2
            self.update()
        elif bridge.bridge_type == Bridge.BRIDGE_TYPE_RED and self.curString == 2 and button == HAL.RED:
            self.curString = 1
            self.update()
        elif bridge.bridge_type == Bridge.BRIDGE_TYPE_YELLOW and self.curString == 2 and button == HAL.YELLOW:
            self.curString = 3
            self.update()
        elif bridge.bridge_type == Bridge.BRIDGE_TYPE_YELLOW and self.curString == 3 and button == HAL.YELLOW:
            self.curString = 2
            self.update()
        elif bridge.bridge_type == Bridge.BRIDGE_TYPE_BLUE and self.curString == 3 and button == HAL.BLUE:
            self.curString = 4
            self.update()
        elif bridge.bridge_type == Bridge.BRIDGE_TYPE_BLUE and self.curString == 4 and button == HAL.BLUE:
            self.curString = 3
            self.update()
        elif bridge.bridge_type == Bridge.BRIDGE_TYPE_ORANGE and self.curString == 4 and button == HAL.ORANGE:
            self.curString = 5
            self.update()
        elif bridge.bridge_type == Bridge.BRIDGE_TYPE_ORANGE and self.curString == 5 and button == HAL.ORANGE:
            self.curString = 4
            self.update()
    
    def update(self):
        #self.rect.move_ip(0,self.guitarStringPaths[self.curString])
        self.rect.topleft = (0,self.guitarStringPaths[self.curString])
        
    def get_rect(self):
        return self.rect
    
    def get_score(self):
        return self.score
    
    def add_score(self, number):
        self.score = self.score + number
        
        