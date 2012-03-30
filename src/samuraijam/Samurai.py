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
from Helpers import *
from pygame.locals import *

class Samurai(pygame.sprite.Sprite):
    """A hero is born!"""
    
    def __init__(self, guitarStrings):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('CTS-sprite.gif',-1)
        self.guitarStrings = guitarStrings
        self.rect.move_ip(0,guitarStrings[2])
        self.curString = 2
    

    def moveToHigher(self,stringNum):
        if stringNum < self.curString:
            self.curString = self.curString -1
            #self.update()
            
    def moveToLower(self, stringNum):
        if stringNum > self.curString:
            self.curString = self.curString + 1
            #self.update()
    
    def update(self):
        #self.rect.move_ip(0,self.guitarStrings[self.curString])
        self.rect.topleft = (0,self.guitarStrings[self.curString])