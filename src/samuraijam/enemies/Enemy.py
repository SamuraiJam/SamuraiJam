import os, sys
import pygame
from samuraijam.util.Helpers import *
from pygame.locals import *

from samuraijam.player.attacks import VerticalSlash

class Enemy(pygame.sprite.Sprite):

    def __init__(self, xPos, yPos):
        pygame.sprite.Sprite.__init__(self) 
        #self.image, self.rect = load_image('pinkcreep.png',-1)
        
        self.image, self.rect = load_image('pinkcreep.png',-1)
        #self.rect = self.image.get_rect()
        
        self.rect.topleft = (xPos,yPos)
        
        self.hit_once = False
        
    def update(self, dist):
        #self.newX = self.newX - 1
        #self.rect.topleft = (self.newX,self.rect.y)
        self.rect.move_ip(-dist,0)
        
    def process_hit(self, attack_type, my_group):
        if attack_type == VerticalSlash.TYPE_VERTICAL_SLASH:
            my_group.remove(self)
        else:
            if not self.hit_once:
                self.hit_once = True
            else:
                my_group.remove(self)
    