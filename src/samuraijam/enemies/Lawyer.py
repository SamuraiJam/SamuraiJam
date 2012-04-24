'''
Created on Apr 24, 2012

@author: Dave
'''

from pygame.sprite import Sprite
from pygame import RLEACCEL
from samuraijam.util.Helpers import *
from samuraijam.player.attacks import VerticalSlash

class Lawyer(Sprite):
    '''
    classdocs
    '''


    def __init__(self, xPos, yPos):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self) 

        self.image, self.rect = load_image_from_folder('lawyer', 'lawyer_1.png', -1)
        
        self.rect.topleft = (xPos,yPos)
        
        #self.images = (load_image_from_folder('groupie_male', 'groupie_male_1.png', -1), load_image_from_folder('groupie_male', 'groupie_male_2.png', -1), load_image_from_folder('groupie_male', 'groupie_male_3.png', -1), load_image_from_folder('groupie_male', 'groupie_male_4.png', -1), load_image_from_folder('groupie_male', 'groupie_male_5.png', -1), load_image_from_folder('groupie_male', 'groupie_male_6.png', -1))
        #self.images = (load_image_from_folder('groupie_female', 'groupie_female_1.png', -1), load_image_from_folder('groupie_female', 'groupie_female_2.png', -1), load_image_from_folder('groupie_female', 'groupie_female_3.png', -1), load_image_from_folder('groupie_female', 'groupie_female_4.png', -1), load_image_from_folder('groupie_female', 'groupie_female_5.png', -1), load_image_from_folder('groupie_female', 'groupie_female_6.png', -1))
        #self.images = (load_image_from_folder('groupie', 'groupie_1.png', -1), load_image_from_folder('groupie', 'groupie_2.png', -1), load_image_from_folder('groupie', 'groupie_3.png', -1), load_image_from_folder('groupie', 'groupie_4.png', -1), load_image_from_folder('groupie', 'groupie_5.png', -1), load_image_from_folder('groupie', 'groupie_6.png', -1), load_image_from_folder('groupie', 'groupie_7.png', -1), load_image_from_folder('groupie', 'groupie_8.png', -1), load_image_from_folder('groupie', 'groupie_9.png', -1))
        
        self.images = load_images_from_folder('lawyer', -1)      
        self.walk_anim = self.images[:3:1]
        self.walk_anim.extend(self.walk_anim[::-1])
                
        self.current_frame = 0
        self.frame_counter = 0
        
        self.hit_once = False
        
    def update(self, dist):
        if self.rect.left < 300:
            self.frame_counter = self.frame_counter + 1
            if self.current_frame < (len(self.images) - 1) and self.frame_counter >= 12:
                self.frame_counter = 0
                self.current_frame = self.current_frame + 1
                    
            self.image, frame_rect = self.images[self.current_frame]
        else:
            self.frame_counter = self.frame_counter + 1
            if self.frame_counter >= 12:
                self.frame_counter = 0
                self.current_frame = self.current_frame + 1
                if self.current_frame > (len(self.walk_anim) - 1):
                    self.current_frame = 0
                    
            self.image, frame_rect = self.walk_anim[self.current_frame]

        
        self.rect.move_ip(-dist,0)
        
    def process_hit(self, attack_type, my_group, update_score_func):
        if attack_type == VerticalSlash.TYPE_VERTICAL_SLASH:
            update_score_func(10)
            my_group.remove(self)
        else:
            if not self.hit_once:
                self.hit_once = True
            else:
                update_score_func(5)
                my_group.remove(self)
                
    def process_player_hit(self, status_bar):
        status_bar.healthBar.update(-20)
        status_bar.update_score(-20)