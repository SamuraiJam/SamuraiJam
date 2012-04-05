'''
Created on Apr 4, 2012

@author: Matt Halpern
'''

import pygame
from threading import Timer

import sys, time, os
from samuraijam.control.HAL import HAL

#from samuraijam.testing.WaitTest import *
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
        self.joy = pygame.joystick.Joystick(0)
        self.joy.init()
        
        #for jay's jank mac
        buttonMap = {11 : HAL.GREEN, 12 : HAL.RED, 13 : HAL.BLUE, 14 : HAL.YELLOW, 8 : HAL.ORANGE, 5 : HAL.BACK, 4 : HAL.START}
        
        #for windows
        #buttonMap = {0 : HAL.GREEN, 1 : HAL.RED, 2 : HAL.BLUE, 3 : HAL.YELLOW, 4 : HAL.ORANGE, 6 : HAL.BACK, 7 : HAL.START}
        axisMap = {4 : HAL.WHAMMY, 2 : HAL.EFFECT, 3 : HAL.TILT}
        hatMap = {0 : { (0, -1) : HAL.STRUM_DOWN, (0, 1) : HAL.STRUM_UP} }
        
        axisDefault = {4 : -1.0}
        hatDefault = {}
        
        self.hal = HAL(buttonMap, axisMap, hatMap, axisDefault, hatDefault)

#        wt = WaitTest(self.gameboard)
#        self.thread = Thread(wt.spawn())

    def game_loop(self):
#        self.thread.start()
        for i in range(0, 10):
            t = Timer(1+i, self.gameboard.add_bridge)
            t.start()
#        self.gameboard.add_bridge()
        start_time = self.default_timer()
        #print start_time
        pre_apocalypse = True
        while pre_apocalypse:
            cur_time = self.default_timer()
            #print cur_time
            #print (cur_time - start_time)
            #print self.gameboard.song_length
            if cur_time >= (self.gameboard.song_length + (self.gameboard.width / self.gameboard.pixels_per_second)):
                pre_apocalypse = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == pygame.JOYBUTTONDOWN:
                    guitarState = self.hal.parseButton(self.joy)
                    self.process_input(guitarState)
                elif event.type == pygame.JOYAXISMOTION:
                    guitarState = self.hal.parseAxis(self.joy)
                    self.process_input(guitarState)
                elif event.type == pygame.JOYHATMOTION:
                    guitarState = self.hal.parseHat(self.joy)
                    self.process_input(guitarState)
                        
            #self.gameboard.bridge_group.update(1)
            self.gameboard.draw()
            pygame.display.flip()
            
    def process_input(self, state):
        print state
        
        if (HAL.STRUM_DOWN in state and state[HAL.STRUM_DOWN] == True) or (HAL.STRUM_UP in state and state[HAL.STRUM_UP] == True):
            buttons_down = ()
            for button in (HAL.GREEN, HAL.RED, HAL.YELLOW, HAL.BLUE, HAL.ORANGE):
                if button in state and state[button] == True:
                    buttons_down.append(button)
            
            num_buttons = len(buttons_down)     
              
            if num_buttons == 1:
                if pygame.sprite.spritecollideany(self.gameboard.samurai, self.gameboard.bridge_group) != None:
                    self.gameboard.samurai.move(buttons_down[0])
            
#        if input == HAL.GREEN:
#            if pygame.sprite.spritecollideany(self.gameboard.samurai, self.gameboard.bridge_group) != None:
#                self.gameboard.samurai.curString = 0
#        elif input == HAL.RED:
#            print "Hal RED"
#            if pygame.sprite.spritecollideany(self.gameboard.samurai, self.gameboard.bridge_group) != None:
#                self.gameboard.samurai.curString = 1
#        elif input == HAL.YELLOW:
#            if pygame.sprite.spritecollideany(self.gameboard.samurai, self.gameboard.bridge_group) != None:
#                self.gameboard.samurai.curString = 2
#        elif input == HAL.BLUE:
#            if pygame.sprite.spritecollideany(self.gameboard.samurai, self.gameboard.bridge_group) != None:
#                self.gameboard.samurai.curString = 3
#        elif input == HAL.ORANGE:
#            if pygame.sprite.spritecollideany(self.gameboard.samurai, self.gameboard.bridge_group) != None:
#                self.gameboard.samurai.curString = 4

if __name__ == '__main__':
    os.chdir(os.path.join("..",".."))
    game = MainGame()
    #game.game_loop()
    
