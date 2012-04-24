'''
Created on Apr 24, 2012

@author: Dave
'''

from pygame.sprite import Sprite
from samuraijam.util.Helpers import *

class FaceMeltingSolo(Sprite):
    '''
    classdocs
    '''

    TYPE_FACE_MELTING_SOLO = "type_face_melting_solo"
    TYPE_MEGA_SWORD = "type_mega_sword"

    def __init__(self,xPos,yPos, killFunction):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self) 
        self.images = load_images_from_folder('face_melting_solo', -1)
        self.images.extend(self.images[::-1])
        self.current_frame = 0
        self.frame_counter = 0
        self.image, self.rect = self.images[0]
        self.rect.topleft = (xPos,yPos)
        self.correct_pos = (xPos, yPos)
        self.killFunction = killFunction
        self.attack_type = self.TYPE_FACE_MELTING_SOLO
        
    def update(self):
        self.frame_counter = self.frame_counter + 1
        
        if self.current_frame == (len(self.images) - 1):
            self.killFunction(self)
        
        if self.frame_counter >= 10:
            self.frame_counter = 0
            self.current_frame = self.current_frame + 1
            
        self.image, self.rect = self.images[self.current_frame]
        self.rect.topleft = self.correct_pos
            