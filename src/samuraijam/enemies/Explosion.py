'''
Created on Apr 24, 2012

@author: Dave
'''

from pygame.sprite import Sprite
from samuraijam.util.Helpers import *


class Explosion(Sprite):
    '''
    classdocs
    '''


    def __init__(self, xPos, yPos, explosion_group):
        '''
        Constructor
        '''

        pygame.sprite.Sprite.__init__(self) 

        self.image, self.rect = load_image_from_folder('mine_explosion', 'explosion_1.png', -1)
        
        self.rect.topleft = (xPos,yPos)
        
        self.explosion = load_images_from_folder('mine_explosion', -1)
        self.explosion_group = explosion_group
        
        self.current_frame = 0
        self.frame_counter = 0
        self.explosion_group.add(self)
        
    def update(self):
        self.frame_counter = self.frame_counter + 1
        if self.current_frame == (len(self.explosion) - 1):
            self.explosion_group.remove(self)
        if self.frame_counter >= 12:
            self.frame_counter = 0
            self.current_frame = self.current_frame + 1
            
                
        self.image, frame_rect = self.explosion[self.current_frame]
        