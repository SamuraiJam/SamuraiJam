'''
Created on Apr 5, 2012

@author: jaywaldron
'''

import threading
import time

class Spawner(threading.Thread):
    '''
    classdocs
    '''


    def __init__(self, file_name, gameboard):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.gameboard = gameboard
        
        self._stop = threading.Event()
        
        level_file = open(file_name, "r")
        self.level = []
        for line in level_file:
            list = line.split()
            self.level.append(list)
            
        level_file.close()
            
        
    def stop(self):
        self._stop.set()
        
    def run(self):
        for list in self.level:
            
            if self._stop.is_set():
                break
            
            #print list[0]
            time.sleep(float(list[0]))
#            if list[1] == '1':
#                self.gameboard.add_bridge()
            for i in range(0,5):
                bridge = int(list[1][i:i+1])
                if bridge == 1:
                    self.gameboard.add_bridge(i)
            for i in range(0, 6):
                enemy = int(list[2][i:i+1])
#                print enemy
                if enemy == 1:
                    self.gameboard.add_mine(i)
                elif enemy == 2:
                    #self.gameboard.add_enemy(i)
                    self.gameboard.add_male_groupie(i)
                    #self.gameboard.add_lawyer(i)
                elif enemy == 3:
                    self.gameboard.add_lawyer(i)
                elif enemy == 4:
                    # fasdfasdf
                    self.gameboard.add_bodyguard(i)
                elif enemy == 5:
                    self.gameboard.add_powerup(i)
