'''
Created on Apr 4, 2012

@author: Matt Halpern
'''

import pygame
import sys, time

from samuraijam.ui import Gameboard

class MainGame(object):


    def __init__(self):
        
        pygame.init()
        
        """Set the window Size"""
        self.width = 1100
        self.height = 600
        
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))
        """Gameboard Time!"""
        self.gameboard = Gameboard(self.screen, self.width, 540, "../../../data/testLevel.txt")
        
        if sys.platform == "win32":
            # On Windows, the best timer is time.clock()
            self.default_timer = time.clock
        else:
            # On most other platforms, the best timer is time.time()
            self.default_timer = time.time

if __name__ == '__main__':
    game = MainGame()
    start_time = game.default_timer()
    pre_apocalypse = True
    while pre_apocalypse:
        cur_time = game.default_timer()
#        print (cur_time - start_time)
        if cur_time >= game.gameboard.song_length:
            pre_apocalypse = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            
        game.gameboard.draw()
        pygame.display.flip()