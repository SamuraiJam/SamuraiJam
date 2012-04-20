'''
Created on Apr 19, 2012

@author: jaywaldron
'''
import os, sys, math
import pygame
from samuraijam.util.Helpers import *
from pygame.locals import *
from samuraijam.control.HAL import HAL


class VerticalSlash(pygame.sprite.Sprite):
    '''
    classdocs
    '''


    def __init__(self,xpos,ypos, killFunction):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)
        #initialization and global variable assignments
        self.base_image, self.rect = load_image('sword.png',-1)
        self.image = self.base_image
        self.killFunction = killFunction
        self.xpos = xpos
        self.ypos = ypos
        
        #start at 75 degrees
        self.image = pygame.transform.rotate(self.image,30)
        self.rect.topleft = (self.xpos,self.ypos)
        self.currentRotation = 75 
    
    def update(self):
        self.currentRotation = self.currentRotation - 10
        if self.currentRotation <= -75:
            self.killFunction(self)
            
        self.image = pygame.transform.rotate(self.base_image,self.currentRotation)
        self.rect = self.image.get_rect()
            
        if self.currentRotation >= 0:
            self.rect.bottomleft = (self.xpos,self.ypos)
        elif self.currentRotation < 0:
            self.rect.bottomright = (self.xpos+self.rect.width,self.ypos+self.rect.height)

        
        