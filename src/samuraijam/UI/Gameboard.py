import os, sys
import pygame
from Helpers import *
from pygame.locals import *

class Gameboard:

    def __init__(self, surface, width, height, guitarStrings):
        """Set the window Size"""
        self.width = width
        self.height = height
        self.surface = surface

                
        """Create the game field (with guitar string paths)"""
        #draw a line from upper-left corner to lower-right corner
        pygame.draw.line(self.surface, (255, 0, 0), (0, guitarStrings[0]), (width, guitarStrings[0]))
        pygame.draw.line(self.surface, (255, 0, 0), (0, guitarStrings[1]), (width, guitarStrings[1]))
        pygame.draw.line(self.surface, (255, 0, 0), (0, guitarStrings[2]), (width, guitarStrings[2]))
        pygame.draw.line(self.surface, (255, 0, 0), (0, guitarStrings[3]), (width, guitarStrings[3]))
        pygame.draw.line(self.surface, (255, 0, 0), (0, guitarStrings[4]), (width, guitarStrings[4]))
        
        #draw background
        pygame.display.flip()
        