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
        
        #start at 90 degrees
        self.image = pygame.transform.rotate(self.image,30)
        self.rect.topleft = (self.xpos,self.ypos)
        #self.image.get_rect().center = (xpos, ypos)
        #print "self.image.get_rect().center: {0}".format(self.image.get_rect().center)
        #print self.xpos
        #print self.ypos
        #self.xpos, self.ypos = self.image.get_rect().center
        self.currentRotation = 75 
    
    def update(self):
        #print self.xpos
        #print self.ypos
        
        self.currentRotation = self.currentRotation - 4
        if self.currentRotation <= -75:
            self.killFunction(self)
            
        self.image = pygame.transform.rotate(self.base_image,self.currentRotation)
        self.rect = self.image.get_rect()
            
        if self.currentRotation >= 0:
            self.rect.bottomleft = (self.xpos,self.ypos)
        elif self.currentRotation < 0:
            self.rect.bottomright = (self.xpos+self.rect.width,self.ypos+self.rect.height)
        #else:
            #self.xpos, self.ypos = self.rect.topleft
            #self.rect.midleft = (self.xpos, self.ypos)
            
            
        '''
        elif self.currentRotation > 0:
            self.image = pygame.transform.rotate(self.base_image,self.currentRotation)
            self.rect = self.image.get_rect()
            #self.rect = self.image.get_rect()
            self.rect.bottomleft = (self.xpos,self.ypos)
        elif self.currentRotation < 0:
            self.image = pygame.transform.rotate(self.base_image,self.currentRotation)
            self.rect = self.image.get_rect()
            #self.rect = self.image.get_rect()
            self.rect.topleft = (self.xpos,self.ypos)
        else:
            self.image = pygame.transform.rotate(self.base_image,self.currentRotation)
            self.rect = self.image.get_rect()
            #self.rect = self.image.get_rect()
            self.rect.midleft = (self.xpos,self.ypos)
        '''    
            
        #calculate where the center should be after next rotation
        #newX = self.xpos + (self.base_image.get_rect().width / 2.0) * math.cos(self.currentRotation)
        #newY = self.ypos - (self.base_image.get_rect().width / 2.0) + ((self.base_image.get_rect().width / 2.0) * math.sin(self.currentRotation))
        '''    
        self.image = pygame.transform.rotate(self.base_image,self.currentRotation)
        self.rect = self.image.get_rect()
        #self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.xpos,self.ypos)
        #self.xpos = newX
        #self.ypos = newY
        '''
        #print self.currentRotation
        #print self.xpos
        #print self.ypos
        
        #self.xpos,self.ypos = (self.xpos - self.image.get_rect().width / 2, self.ypos - self.image.get_rect().height / 2)
        #get new position for upper left corner for rotated image
        
        #self.rect.topleft = (self.xpos,self.ypos)

        #self.image = pygame.transform.rotate(self.base_image,self.currentRotation)
        
        
        
        
        
        
        
        
        