'''
Created on Apr 4, 2012

@author: Matt Halpern
'''
import time
from samuraijam.ui.Gameboard import Gameboard

class WaitTest:
    
    def __init__(self, gameboard):
        self.gameboard = gameboard
        
    def spawn(self):
        for i in range(0, 10):
            time.sleep(1)
            self.gameboard.add_bridge()