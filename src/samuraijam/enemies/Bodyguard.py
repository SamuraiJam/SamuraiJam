'''
Created on Apr 24, 2012

@author: Dave
'''

from samuraijam.util.Helpers import *
from pygame.sprite import Sprite
from samuraijam.player.attacks.FireSword import FireSword

class Bodyguard(Sprite):
    '''
    classdocs
    '''


    def __init__(self, xPos, yPos):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self) 

        self.image, self.rect = load_image_from_folder('guard', 'guard.png', -1)
        
        self.rect.topleft = (xPos,yPos)
        
        self.hit_once = False
        
        
    def update(self, dist):
        self.rect.move_ip(-dist,0)
        
    def process_hit(self, attack_type, my_group, update_score_func):
        if attack_type == FireSword.TYPE_FIRE_SWORD:
            update_score_func(10)
            my_group.remove(self)
        else:
            if not self.hit_once:
                self.hit_once = True
            else:
                update_score_func(5)
                my_group.remove(self)
                
    def process_player_hit(self, status_bar, samurai):
        status_bar.healthBar.update(-20)
        samurai.stun(status_bar)