import os, sys
import pygame
#from Helpers import *
from pygame.locals import *
from samuraijam.spriteParts import *

class OldGameboard:

    def __init__(self, surface, width, height, guitarStrings):
        """Set the window Size"""
        self.width = width
        self.height = height
        self.surface = surface

                
        """Create the game field (with guitar string paths)"""
        #draw a line from upper-left corner to lower-right corner
        '''
        pygame.draw.line(self.surface, (255, 0, 0), (0, guitarStrings[0]), (width, guitarStrings[0]))
        pygame.draw.line(self.surface, (255, 0, 0), (0, guitarStrings[1]), (width, guitarStrings[1]))
        pygame.draw.line(self.surface, (255, 0, 0), (0, guitarStrings[2]), (width, guitarStrings[2]))
        pygame.draw.line(self.surface, (255, 0, 0), (0, guitarStrings[3]), (width, guitarStrings[3]))
        pygame.draw.line(self.surface, (255, 0, 0), (0, guitarStrings[4]), (width, guitarStrings[4]))
        '''
        
        #draw the 6 paths
        pathWidth = 96
        pathHeight = 48
        self.paths = []
        for location in [
                [0, guitarStrings[0]],[pathWidth, guitarStrings[0]],[pathWidth*2, guitarStrings[0]],[pathWidth*3, guitarStrings[0]],[pathWidth*4, guitarStrings[0]],[pathWidth*5, guitarStrings[0]],
                 [0, guitarStrings[1]],[pathWidth, guitarStrings[1]],[pathWidth*2, guitarStrings[1]],[pathWidth*3, guitarStrings[1]],[pathWidth*4, guitarStrings[1]],[pathWidth*5, guitarStrings[1]],
                 [0, guitarStrings[2]],[pathWidth, guitarStrings[2]],[pathWidth*2, guitarStrings[2]],[pathWidth*3, guitarStrings[2]],[pathWidth*4, guitarStrings[2]],[pathWidth*5, guitarStrings[2]],
                 [0, guitarStrings[3]],[pathWidth, guitarStrings[3]],[pathWidth*2, guitarStrings[3]],[pathWidth*3, guitarStrings[3]],[pathWidth*4, guitarStrings[3]],[pathWidth*5, guitarStrings[3]],
                 [0, guitarStrings[4]],[pathWidth, guitarStrings[4]],[pathWidth*2, guitarStrings[4]],[pathWidth*3, guitarStrings[4]],[pathWidth*4, guitarStrings[4]],[pathWidth*5, guitarStrings[4]],
                 [0, guitarStrings[5]],[pathWidth, guitarStrings[5]],[pathWidth*2, guitarStrings[5]],[pathWidth*3, guitarStrings[5]],[pathWidth*4, guitarStrings[5]],[pathWidth*5, guitarStrings[5]]
                 ]:
            self.paths.append(DirtPath(location))
        
        
        #draw background
        #pygame.display.flip()
        
        for b in self.paths:
            #b.update(time, 150)
            surface.blit(b.image, b.rect)
        
        pygame.display.update()
        