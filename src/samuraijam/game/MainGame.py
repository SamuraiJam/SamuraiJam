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
from samuraijam.player.attacks.FaceMeltingSolo import FaceMeltingSolo
from samuraijam.player.attacks.WaterSpray import WaterSpray
from samuraijam.player.attacks.FireSword import FireSword
from samuraijam.util import *
from samuraijam.game.LevelPauseMenu import *
from samuraijam.game.WinScreen import *

class MainGame(object):


    def __init__(self, level, screen=None):
        
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
        
        
#        self.statusBar = StatusBar(surface=self.screen,color=(200, 200, 200),width=self.width,height=60,x=0,y=0)
        
        """Gameboard Time!"""
        #load_level = os.path.join('..', 'data', 'songs', 'sexy.txt')
        self.gameboard = Gameboard(self.screen, self.width, 540, level)
        
        self.statusBar = StatusBar(surface=self.screen, color=(200, 200, 200), width=self.width, height=60, x=0, y=0, song_name=self.gameboard.song_name)
        
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
            
            
        full_music_path = os.path.join('..', 'data', 'music', self.gameboard.music_filename)
        
        print "Trying to load " + os.path.abspath(full_music_path)
        load_path = os.path.abspath(full_music_path.strip('\n'))
        print load_path
        pygame.mixer.music.load(full_music_path)
        
        # Where are the sound effects?
        self.sound_basic_slash = load_sound_from_folder('sound_effects', 'vertical_slash.wav')
        self.sound_face_melt = load_sound_from_folder('sound_effects', 'face_melt.wav')
        self.sound_fire_sword = load_sound_from_folder('sound_effects', 'fire_sword.wav')
        self.sound_water_spray = load_sound_from_folder('sound_effects', 'water_spray.wav')
        self.sound_mine_explosion = load_sound_from_folder('sound_effects', 'mine_explosion.wav')
        self.sound_mega_sword_get = load_sound_from_folder('sound_effects', 'mega_sword_get.wav')
        self.sound_generic_powerup = load_sound_from_folder('sound_effects', 'powerup.wav')
        self.sound_scream = load_sound_from_folder('sound_effects', 'WilhelmScream.ogg')
        
        
        """Joystick"""
        self.joy = pygame.joystick.Joystick(0)
        self.joy.init()
        
        self.hal = HAL(self.buttonMap, self.axisMap, self.hatMap, self.axisDefault, self.hatDefault)
        
        self.is_playing = False
#        self.health = 100

#        wt = WaitTest(self.gameboard)
#        self.thread = Thread(wt.spawn())

    def game_loop(self):
#        self.thread.start()
#        for i in range(0, 10):
#            t = Timer(1+i, self.gameboard.add_bridge)
#            t.start()
#        self.gameboard.add_bridge()
        self.gameboard.add_healthpack(3)

        full_level_path = os.path.join('..', 'data', 'levels', self.gameboard.level_filename)

        spawner = Spawner(full_level_path, self.gameboard)
        spawner.start()
        start_time = self.default_timer()
        #print start_time
        
        start_music = Timer(1025.0 / self.gameboard.pixels_per_second, self.playSexy)
        start_music.start()
        pre_apocalypse = True
        complete = False
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
                    spawner.stop()
                    pygame.quit()
                    sys.exit()
                elif event.type == Constants.Song_End_Event:
                    pre_apocalypse = False
                    complete = True
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
                        
#            if self.is_playing == False and pygame.sprite.spritecollideany(self.gameboard.samurai, self.gameboard.bridge_group) != None:
#                self.playSexy()       
                
                
            # Process attacks before player impacts:
            
            enemy_a_collosions = pygame.sprite.groupcollide(self.gameboard.attack_group, self.gameboard.enemy_group, False, False).items()
            if enemy_a_collosions != None:
                for attack, enemies in enemy_a_collosions:
                    for enemy in enemies:
                        enemy.process_hit(attack.attack_type, self.gameboard.enemy_group, self.statusBar)
                    self.gameboard.attack_group.remove(attack)

                        
            mine_p_collisions = pygame.sprite.spritecollide(self.gameboard.samurai, self.gameboard.mine_group, False)
            if mine_p_collisions != None:
                for m in mine_p_collisions:
                    self.gameboard.add_explosion(m.rect.top)
                    self.sound_mine_explosion.play()
                    
                    if not self.gameboard.samurai.is_invincible:
                        m.process_player_hit(self.statusBar)
                    
                    self.gameboard.mine_group.remove(m)
                    if self.statusBar.healthBar.curValue <= 0:
                        pre_apocalypse = False
            
            enemy_p_collisions = pygame.sprite.spritecollide(self.gameboard.samurai, self.gameboard.enemy_group, False)
            if enemy_p_collisions != None:
                for e in enemy_p_collisions:
                    if not self.gameboard.samurai.is_invincible:
                        self.sound_scream.play()
                        e.process_player_hit(self.statusBar, self.gameboard.samurai)
                    self.gameboard.enemy_group.remove(e)
                    if self.statusBar.healthBar.curValue <= 0:
                        pre_apocalypse = False
                        
            ## check for powerup collisions ##
            healthpack_p_collisions = pygame.sprite.spritecollide(self.gameboard.samurai, self.gameboard.healthpack_group, False)
            if healthpack_p_collisions != None:
                for m in healthpack_p_collisions:
                    self.sound_generic_powerup.play()
                    self.gameboard.healthpack_group.remove(m)
                    self.statusBar.healthBar.update(30)
                    
                    
            ki_potion_p_collisions = pygame.sprite.spritecollide(self.gameboard.samurai, self.gameboard.ki_potion_group, False)
            if ki_potion_p_collisions != None:
                for m in ki_potion_p_collisions:
                    self.sound_generic_powerup.play()
                    self.gameboard.ki_potion_group.remove(m)
                    self.statusBar.kiBar.update(30)
                    
            shield_p_collisions = pygame.sprite.spritecollide(self.gameboard.samurai, self.gameboard.shield_group, False)
            if shield_p_collisions != None:
                for s in shield_p_collisions:
                    self.sound_generic_powerup.play()
                    self.gameboard.samurai.ha_I_am_invincible(self.statusBar)
                    self.gameboard.shield_group.remove(s)
                    
            sword_p_collisions = pygame.sprite.spritecollide(self.gameboard.samurai, self.gameboard.sword_group, False)
            if sword_p_collisions != None:
                for s in sword_p_collisions:
                    self.sound_mega_sword_get.play()
                    self.gameboard.samurai.mega_sword_get(self.statusBar)
                    self.gameboard.sword_group.remove(s)
            
                    #add score!
            
            self.gameboard.draw()
            pygame.display.flip()
        
#        spawner.stop()
        time_played = pygame.mixer.music.get_pos()
        if pygame.mixer.music.get_busy:
            pygame.mixer.music.stop()
        if complete:
            percent_played = 100
        else:
            percent_played = int(time_played/(10*self.gameboard.song_length))
        m = WinScreen(self.screen)
        m.mainLoop(self.gameboard.level_filename, self.statusBar.score, percent_played)
            
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
                
                if (HAL.GREEN in state and state[HAL.GREEN] == True) and (HAL.RED in state and state[HAL.RED] == True):
#                    self.statusBar.kiBar.update(-2)
                    my_attack = VerticalSlash(tempRect.centerx,tempRect.centery, self.gameboard.remove_attack)
                    
                    if self.gameboard.samurai.has_mega_sword:
                        my_attack.attack_type = VerticalSlash.TYPE_MEGA_SWORD
                    
                    self.gameboard.add_attack(my_attack)
                    self.sound_basic_slash.play()
                
                elif (self.statusBar.kiBar.curValue >= 20) and (HAL.GREEN in state and state[HAL.GREEN] == True) and (HAL.YELLOW in state and state[HAL.YELLOW] == True):
                    self.statusBar.kiBar.update(-20)
                    
                    my_attack = FaceMeltingSolo(tempRect.centerx - 20, tempRect.centery - 20, self.gameboard.remove_attack)
                    
                    if self.gameboard.samurai.has_mega_sword:
                        my_attack.attack_type = VerticalSlash.TYPE_MEGA_SWORD
                    
                    self.gameboard.add_attack(my_attack)
                    self.sound_face_melt.play()
                    
                elif (self.statusBar.kiBar.curValue >= 20) and (HAL.GREEN in state and state[HAL.GREEN] == True) and (HAL.BLUE in state and state[HAL.BLUE] == True):
                    self.statusBar.kiBar.update(-20)
                    
                    my_attack = WaterSpray(tempRect.centerx + 10, tempRect.centery - 10, self.gameboard.remove_attack)
                    
                    if self.gameboard.samurai.has_mega_sword:
                        my_attack.attack_type = VerticalSlash.TYPE_MEGA_SWORD
                    
                    self.gameboard.add_attack(my_attack)
                    self.sound_water_spray.play()
                    
                elif (self.statusBar.kiBar.curValue >= 20) and (HAL.RED in state and state[HAL.RED] == True) and (HAL.YELLOW in state and state[HAL.YELLOW] == True):
                    self.statusBar.kiBar.update(-20)
                    
                    my_attack = FireSword(tempRect.centerx, tempRect.centery, self.gameboard.remove_attack)
                    
                    if self.gameboard.samurai.has_mega_sword:
                        my_attack.attack_type = VerticalSlash.TYPE_MEGA_SWORD
                    
                    self.gameboard.add_attack(my_attack)
                    self.sound_fire_sword.play()
                    
                    
            
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
    
