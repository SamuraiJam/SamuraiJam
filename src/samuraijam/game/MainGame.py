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
from samuraijam.enemy_spawn.Spawner import Spawner
from samuraijam.player.attacks import *
from samuraijam.util import *
from samuraijam.game.LevelPauseMenu import *

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
        
        if sys.platform == "darwin":
            self.buttonMap = {11 : HAL.GREEN, 12 : HAL.RED, 13 : HAL.BLUE, 14 : HAL.YELLOW, 8 : HAL.ORANGE, 5 : HAL.BACK, 4 : HAL.START, 1 : HAL.STRUM_DOWN, 0 : HAL.STRUM_UP}
        
            self.axisMap = {4 : HAL.WHAMMY, 1 : HAL.EFFECT, 5 : HAL.TILT, 2 : HAL.NOTHING, 3 : HAL.NOTHING}
            
            self.hatMap = {0 : {} }
            
            self.axisDefault = {4 : -1.0}
            self.hatDefault = {}
            
        elif sys.platform == "win32":
            self.buttonMap = {0 : HAL.GREEN, 1 : HAL.RED, 2 : HAL.BLUE, 3 : HAL.YELLOW, 4 : HAL.ORANGE, 6 : HAL.BACK, 7 : HAL.START}
            self.axisMap = {4 : HAL.WHAMMY, 2 : HAL.EFFECT, 3 : HAL.TILT}
            
            self.hatMap = {0 : { (0, -1) : HAL.STRUM_DOWN, (0, 1) : HAL.STRUM_UP} }
            
            self.axisDefault = {4 : -1.0}
            self.hatDefault = {}
            
        pygame.mixer.music.load(os.path.join('..', 'data', "sexyAndIKnowIt.ogg"))
        
        """Joystick"""
        self.joy = pygame.joystick.Joystick(0)
        self.joy.init()
        
        self.hal = HAL(self.buttonMap, self.axisMap, self.hatMap, self.axisDefault, self.hatDefault)
        
        self.is_playing = False
        self.health = 100

#        wt = WaitTest(self.gameboard)
#        self.thread = Thread(wt.spawn())

    def game_loop(self):
#        self.thread.start()
#        for i in range(0, 10):
#            t = Timer(1+i, self.gameboard.add_bridge)
#            t.start()
#        self.gameboard.add_bridge()
        self.gameboard.add_healthpack(3)

        spawner = Spawner("../data/sexy-level.txt", self.gameboard)
        spawner.start()
        start_time = self.default_timer()
        #print start_time
        pre_apocalypse = True
        while pre_apocalypse:
            #cur_time = self.default_timer()
            #print cur_time
            #print (cur_time - start_time)
            #print self.gameboard.song_length
            #if cur_time >= (self.gameboard.song_length + (self.gameboard.width / self.gameboard.pixels_per_second)):
            #    pre_apocalypse = False
                
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
                elif event.type == Constants.Song_End_Event:
                    pre_apocalypse = False
                elif sys.platform == "darwin" and event.type == pygame.JOYBUTTONDOWN:
                    guitarState = self.hal.parseButton(self.joy)
                    self.process_pause(guitarState)
                    self.process_input(guitarState)
#                elif event.type == pygame.JOYAXISMOTION:
#                    guitarState = self.hal.parseAxis(self.joy)
#                    self.process_input(guitarState)
                elif sys.platform == "win32" and event.type == pygame.JOYHATMOTION:
                    guitarState = self.hal.parseAll(self.joy)
                    self.process_input(guitarState)
                elif sys.platform == "win32" and event.type == pygame.JOYBUTTONDOWN:
                    guitarState = self.hal.parseButton(self.joy)
                    self.process_pause(guitarState)
                        
            if self.is_playing == False and pygame.sprite.spritecollideany(self.gameboard.samurai, self.gameboard.bridge_group) != None:
                self.playSexy()       
                
                
            # Process attacks before player impacts:
            
            enemy_a_collosions = pygame.sprite.groupcollide(self.gameboard.attack_group, self.gameboard.enemy_group, False, False).items()
            if enemy_a_collosions != None:
                for attack, enemies in enemy_a_collosions:
                    for enemy in enemies:
                        enemy.process_hit(attack.attack_type, self.gameboard.enemy_group, self.statusBar.update_score)
                    self.gameboard.attack_group.remove(attack)
                    
#                    enemy.process_hit(attack.attack_type, self.gameboard.enemy_group)
                        
            mine_p_collisions = pygame.sprite.spritecollide(self.gameboard.samurai, self.gameboard.mine_group, False)
            if mine_p_collisions != None:
                for m in mine_p_collisions:
                    self.gameboard.add_explosion(m.rect.top)
                    self.gameboard.mine_group.remove(m)
                    self.health = self.health - 10
                    self.statusBar.healthBar.update(-10)
                    if self.health <= 0:
                        pre_apocalypse = False
            
            enemy_p_collisions = pygame.sprite.spritecollide(self.gameboard.samurai, self.gameboard.enemy_group, False)
            if enemy_p_collisions != None:
                for e in enemy_p_collisions:
                    self.gameboard.enemy_group.remove(e)
                    self.health = self.health - 20
                    self.statusBar.healthBar.update(-20)
                    if self.health <= 0:
                        pre_apocalypse = False
                        
            ## check for powerup collisions ##
            healthpack_p_collisions = pygame.sprite.spritecollide(self.gameboard.samurai, self.gameboard.healthpack_group, False)
            if healthpack_p_collisions != None:
                for m in healthpack_p_collisions:
                    self.gameboard.healthpack_group.remove(m)
                    self.health = self.health + 30
                    self.health = min(self.health, 100)
                    self.statusBar.healthBar.update(30)

                        
            
                    #add score!
            
            self.gameboard.draw()
            pygame.display.flip()
            
            
    def process_pause(self, state):
        #check for pause menu
        if HAL.START in state and state[HAL.START] == True:
            wasPaused = False
            if pygame.mixer.music.get_busy:
                pygame.mixer.music.pause()
                wasPaused = True
            m = LevelPauseMenu(self.screen)
            m.mainLoop()
            #Constants.sexyMusic.stop()
            #check to see if we're quitting forever
            if m.timeToQuit():
                pre_apocalypse = False
            else:
                #reblit the status info
                self.statusBar.draw() #redraw this since it won't be blitted again
                if wasPaused:
                    pygame.mixer.music.unpause();
                self.gameboard.last_frame_time = self.gameboard.default_timer()     # Hax, don't count the time spent pausing.        
    
    def process_input(self, state):
        print state
        
        if (HAL.STRUM_DOWN in state and state[HAL.STRUM_DOWN] == True) or (HAL.STRUM_UP in state and state[HAL.STRUM_UP] == True):
            buttons_down = []
            for button in (HAL.GREEN, HAL.RED, HAL.YELLOW, HAL.BLUE, HAL.ORANGE):
                if button in state and state[button] == True:
                    buttons_down.append(button)
            
            num_buttons = len(buttons_down)     
              
            if num_buttons == 1:
#                if pygame.sprite.spritecollideany(self.gameboard.samurai, self.gameboard.bridge_group) != None:
#                    self.gameboard.samurai.move(buttons_down[0])
                bridge_collisions = pygame.sprite.spritecollide(self.gameboard.samurai, self.gameboard.bridge_group, False, None)
                if bridge_collisions != None:
                    for bridge in bridge_collisions:
                        self.gameboard.samurai.move(buttons_down[0], bridge)
            if num_buttons == 2:
                tempSprite = self.gameboard.samurai_sprite_group.sprites()
                tempRect = tempSprite[0].get_rect()
                self.gameboard.add_attack(VerticalSlash(tempRect.centerx,tempRect.centery, self.gameboard.remove_attack))
            
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

    def playSexy(self):
        self.is_playing = True
        pygame.mixer.music.set_endevent(Constants.Song_End_Event)
        pygame.mixer.music.play()
        #Constants.sexyMusic = load_sound("sexyAndIKnowIt.ogg")
        #Constants.sexyMusic.play()
            
            
            
if __name__ == '__main__':
    os.chdir(os.path.join("..",".."))
    game = MainGame()
    #game.game_loop()
    
