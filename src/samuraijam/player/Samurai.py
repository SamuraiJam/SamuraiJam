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
        self.images = (load_samurai_image('chr06164.BMP', -1), load_samurai_image('chr06166.BMP', -1), load_samurai_image('chr06167.BMP', -1), load_samurai_image('chr06168.BMP', -1), load_samurai_image('chr06169.BMP', -1), load_samurai_image('chr06170.BMP', -1), load_samurai_image('chr06171.BMP', -1), load_samurai_image('chr06172.BMP', -1))
        self.current_frame = 0
        self.frame_counter = 0
        self.guitarStringPaths = guitarStrings
        self.rect.move_ip(0,guitarStrings[2])
        self.curString = 2
    

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
        self.frame_counter = self.frame_counter + 1
        if self.frame_counter >= 10:
            self.frame_counter = 0
            self.current_frame = self.current_frame + 1
            if self.current_frame > len(self.images):
                self.current_frame = 0
        self.image, self.rect = self.images[self.current_frame]
        
    def get_rect(self):
        return self.rect