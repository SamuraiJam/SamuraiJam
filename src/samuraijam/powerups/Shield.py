'''
Created on Apr 23, 2012

@author: Boris Grishenko
'''

from samuraijam.util.Helpers import *
from pygame.sprite import Sprite

class Shield(Sprite):
    '''
    classdocs
    '''
    def __init__(self, xPos, yPos):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self) 
               
        self.image, self.rect = load_image_from_folder('powerups', 'shield_pickup.png',-1)

        self.rect.topleft = (xPos,yPos)


    def update(self, dist):
        self.rect.move_ip(-dist,0)
    
        