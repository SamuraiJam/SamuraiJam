'''
Created on Apr 23, 2012

@author: Dave Lee, king of the Ki
'''

from samuraijam.util.Helpers import *
from pygame.sprite import Sprite

class MegaSword(Sprite):
    '''
    classdocs
    '''
    def __init__(self, xPos, yPos):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self) 
               
        self.image, self.rect = load_image_from_folder('powerups', 'sword_pickup.png',-1)

        self.rect.topleft = (xPos,yPos)


    def update(self, dist):
        self.rect.move_ip(-dist,0)
    
        