'''
Created on Apr 4, 2012

@author: Matt Halpern
'''
import time
import threading
from samuraijam.ui import Gameboard

class WaitTest:
    
    def __init__(self, gameboard):
        self.gameboard = gameboard
        
    def run(self):
        for i in range(0, 10):
            time.sleep(1)
            self.gameboard.add_bridge()