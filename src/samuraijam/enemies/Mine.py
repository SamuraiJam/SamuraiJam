'''
Created on Apr 5, 2012

@author: jaywaldron
'''

import pygame
from samuraijam.util import *

class Mine(pygame.sprite.Sprite):
    


    def __init__(self, xPos, yPos):
        
        pygame.sprite.Sprite.__init__(self) 
        #self.image, self.rect = load_image('pinkcreep.png',-1)
        
        self.image, self.rect = load_image_from_folder('mine_blink', 'mine_1.png', -1) #load_image('graycreep.png',-1)
        
        #self.rect = self.image.get_rect()
        
        self.rect.topleft = (xPos,yPos)
        
        self.blink_anim = load_images_from_folder('mine_blink', -1)
        self.current_frame = 0
        self.frame_counter = 0
        
        
    def update(self, dist):
        #self.newX = self.newX - 1
        #self.rect.topleft = (self.newX,self.rect.y)
        
        self.frame_counter = self.frame_counter + 1
        if self.frame_counter >= 40:
            self.frame_counter = 0
            self.current_frame = self.current_frame + 1
            if self.current_frame > (len(self.blink_anim) - 1):
                self.current_frame = 0
                
        self.image, frame_rect = self.blink_anim[self.current_frame]
        
        
        self.rect.move_ip(-dist,0)
        
    def process_player_hit(self, status_bar):
        status_bar.healthBar.update(-10)