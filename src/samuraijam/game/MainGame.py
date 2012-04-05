'''
Created on Apr 4, 2012

@author: Matt Halpern
'''

import pygame
from threading import Thread

import sys, time, os
from samuraijam.control.HAL import HAL

#import samuraijam.testing.WaitTest
from samuraijam.ui import Gameboard, StatusBar

class MainGame(object):


    def __init__(self, screen=None):
        
        """Set the window Size"""
        self.width = 1100
        self.height = 600
        
        """Create the Screen"""
        if screen == None:
            pygame.init()
            self.screen = pygame.display.set_mode((self.width, self.height))
        else:
            self.screen = screen
        screen.fill((0,0,0))
        
        
        self.statusBar = StatusBar(surface=self.screen,color=(200, 200, 200),width=self.width,height=60,x=0,y=0)
        
        """Gameboard Time!"""
        self.gameboard = Gameboard(self.screen, self.width, 540, "../data/testLevel.txt")
        
        if sys.platform == "win32" or sys.platform == "darwin":
            # On Windows, the best timer is time.clock()
            self.default_timer = time.clock
        else:
            # On most other platforms, the best timer is time.time()
            self.default_timer = time.time            
        
        """Joystick"""
        #self.joy = pygame.joystick.Joystick(0)
        #self.joy.init()
        
        buttonMap = {0 : HAL.GREEN, 1 : HAL.RED, 2 : HAL.BLUE, 3 : HAL.YELLOW, 4 : HAL.ORANGE, 6 : HAL.BACK, 7 : HAL.START}
        axisMap = {4 : HAL.WHAMMY, 2 : HAL.EFFECT, 3 : HAL.TILT}
        hatMap = {0 : HAL.STRUM}
        
        axisDefault = {4 : -1.0}
        hatDefault = {}
        
        self.hal = HAL(buttonMap, axisMap, hatMap, axisDefault, hatDefault)

#        wt = WaitTest(self.gameboard)
#        self.thread = Thread(wt.spawn())

    def game_loop(self):
#        self.thread.start()
        self.gameboard.add_bridge()
        start_time = self.default_timer()
        #print start_time
        pre_apocalypse = True
        while pre_apocalypse:
            cur_time = self.default_timer()
            #print cur_time
            #print (cur_time - start_time)
            #print self.gameboard.song_length
            if cur_time >= self.gameboard.song_length:
                pre_apocalypse = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == pygame.JOYBUTTONDOWN:
                    guitarState = self.hal.parseButton(self.joy)
                    for key, value in guitarState.iteritems():
                        #print "{0} is {1}".format(key, value)
                        self.process_input(key, value)
                elif event.type == pygame.JOYAXISMOTION:
                    guitarState = self.hal.parseAxis(self.joy)
                    for key, value in guitarState.iteritems():
                        #print "{0} is {1}".format(key, value)
                        self.process_input(key, value)
                elif event.type == pygame.JOYHATMOTION:
                    guitarState = self.hal.parseHat(self.joy)
                    for key, value in guitarState.iteritems():
                        #print "{0} is {1}".format(key, value)
                        self.process_input(key, value)
                        
            self.gameboard.draw()
            pygame.display.flip()
            
    def process_input(self, input, value):
        
        if input == HAL.GREEN:
            if pygame.sprite.spritecollideany(self.gameboard.samurai, self.gameboard.bridge_group) != None:
                self.gameboard.samurai.curString = 0
        elif input == HAL.RED:
            if pygame.sprite.spritecollideany(self.gameboard.samurai, self.gameboard.bridge_group) != None:
                self.gameboard.samurai.curString = 1
        elif input == HAL.YELLOW:
            if pygame.sprite.spritecollideany(self.gameboard.samurai, self.gameboard.bridge_group) != None:
                self.gameboard.samurai.curString = 2
        elif input == HAL.BLUE:
            if pygame.sprite.spritecollideany(self.gameboard.samurai, self.gameboard.bridge_group) != None:
                self.gameboard.samurai.curString = 3
        elif input == HAL.ORANGE:
            if pygame.sprite.spritecollideany(self.gameboard.samurai, self.gameboard.bridge_group) != None:
                self.gameboard.samurai.curString = 4

if __name__ == '__main__':
    os.chdir(os.path.join("..",".."))
    game = MainGame()
    #game.game_loop()
    
