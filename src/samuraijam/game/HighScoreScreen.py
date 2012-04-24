'''
Created on Apr 24, 2012

@author: Matt Halpern
'''

import sys, os, time, pygame
from pygame.locals import *
from samuraijam.util import *
from samuraijam.control.HAL import *
#from samuraijam.game import *
#from menu import *
#from samuraijam.game import LevelSelectMenu
#from LevelSelectMenu import *
from menu import *
from LevelSelectMenu import *
from pygame.font import Font


class HighScoreScreen:
    def __init__(self, screen):
        """Initialize PyGame"""
        #pygame.init()
        self.screen = screen
        self.name = ''

    def mainLoop(self):
                    
        screen = self.screen
        """Joystick"""
        self.joy=pygame.joystick.Joystick(0)
        self.joy.init()
        #self.numbutton = self.joy.get_numbuttons()
        
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
            
        self.hal = HAL(self.buttonMap, self.axisMap, self.hatMap, self.axisDefault, self.hatDefault)
        
        '''Sounds!'''
        self.clashingSwords = load_sound("swords_1Clash.ogg")
        
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        
        """Create the Screen"""
        #screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        #self.mainScreenBackground, self.mainScreenBackgroundRect = load_image("SamuraiJam_MainScreen.jpg")
        #mainScreenBackground = pygame.image.load("../../data/SamuraiJam_MainScreen.jpg")
        #mainScreenBackgroundRect = mainScreenBackground.get_rect()
        #blit once first to avoid graphics conflicts with the menu
        #screen.blit(mainScreenBackground, mainScreenBackgroundRect)
        #screen.fill((255,255,255))
        #mainScreenBackground,mainScreenBackgroundRect = load_image("samuraiFlute.jpg")
        #mainScreenBackgroundRect = mainScreenBackground.get_rect()
        #blit once first to avoid graphics conflicts with the menu
        #screen.blit(mainScreenBackground, (700,0))
        
        #create a translucent overlay
        self.winSurface = pygame.Surface((screen.get_width(),screen.get_height()))  # the size of your rect
        self.winSurface.set_alpha(255)                # alpha level
        self.winSurface.fill((255,255,255))           # this fills the entire surface
        screen.blit(self.winSurface, (0,0))    # (0,0) are the top-left coordinates
        
        
        font = Font(None, 60)
        text = font.render("NEW HIGH SCORE!!!", 1, (0,0,0))
        screen.blit(text, (350,50))
        text = font.render("Enter your initials:", 1, (0,0,0))
        screen.blit(text, (345, 100))
        
        font = Font(None, 40)
        for i in range(0, 3):
            letter = 'A'
            done = False
            while not done:
                text = font.render(letter, 1, (0,0,0), (255,255,255))
                screen.blit(text, (400 + 25*i, 150))
                e = pygame.event.wait()
                        
                if sys.platform == "win32":
                    if e.type == pygame.JOYHATMOTION:
                        g_state = self.hal.parseAll(self.joy)
                        if (HAL.STRUM_DOWN in g_state and g_state[HAL.STRUM_DOWN] == True):
                            e = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_DOWN)
                        elif (HAL.STRUM_UP in g_state and g_state[HAL.STRUM_UP] == True):
                            e = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_UP)
                    elif e.type == pygame.JOYBUTTONDOWN:
                        g_state = self.hal.parseButton(self.joy)
                        if (HAL.GREEN in g_state) and (g_state[HAL.GREEN] == True):
                            e = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_RETURN)
                            
                elif sys.platform == "darwin":
                    if e.type == pygame.JOYBUTTONDOWN:
                        g_state = self.hal.parseButton(self.joy)
                        if (HAL.STRUM_DOWN in g_state and g_state[HAL.STRUM_DOWN] == True):
                            e = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_DOWN)
                        elif (HAL.STRUM_UP in g_state and g_state[HAL.STRUM_UP] == True):
                            e = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_UP)
                        elif (HAL.GREEN in g_state) and (g_state[HAL.GREEN] == True):
                            e = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_RETURN)
                
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_DOWN:
                        dec = ord(letter) + 1
                        if dec > 90:
                            dec = dec - 26
                        letter = chr(dec)
                    elif e.key == pygame.K_UP:
                        dec = ord(letter) - 1
                        if dec < 65:
                            dec = dec +26
                        letter = chr(dec)
                    elif e.key == pygame.K_RETURN:
                        done = True
            self.name = self.name + letter
                
        
                
if __name__ == "__main__":
    HighScoreScreen()
    
    