'''
Created on Apr 4, 2012

@author: Matt Halpern
'''

import pygame

class Bridge(object):
    


    def __init__(self, xPos, yPos):
        
        pygame.sprite.Sprite.__init__(self) 
        #self.image, self.rect = load_image('pinkcreep.png',-1)
        
        self.image = pygame.image.load('../../../data/bluecreep.png')
        self.rect = self.image.get_rect()
        
        self.rect.topleft = (xPos,yPos)
        
    def update(self, dist):
        #self.newX = self.newX - 1
        #self.rect.topleft = (self.newX,self.rect.y)
        self.rect.move_ip(-dist,0)