'''
Created on Apr 24, 2012

@author: jaywaldron
'''
import sys, os, time, pygame
from pygame.locals import *
from samuraijam.util import *
#from samuraijam.game import *
#from menu import *
#from samuraijam.game import LevelSelectMenu
#from LevelSelectMenu import *
from menu import *
from LevelSelectMenu import *

class IntroMovie:
    def __init__(self,screen=None):
        '''
        Constructor
        '''
        
        """Initialize PyGame"""
        pygame.init()
        self.screen = screen
        
        """Joystick"""
        '''
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
        '''
        
        
    def mainLoop(self):
        
        # Initialize the mixer
        #pygame.mixer.init()
        
        #pygame.mixer.music.load("../../data/introFlute.ogg")
        #pygame.mixer.music.play(0, 0.0)
        screen = self.screen
        """Create the Screen"""
        if screen==None:
            screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            
        # Ignore mouse motion (greatly reduces resources when not needed)
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        
        ##### play intro video here #####
        #path = "../data/movie.mpg"
        self.path = os.path.join('..','data','movie.mpg')
        os.system("vlc "+self.path)
        #introMovie = pygame.movie.Movie(self.path)
        #introMovie.set_display(screen)
        #introMovie.play()
        print "playing"
    
        #while introMovie.get_busy:
    
        '''
        # The main while loop
        while 1:
            # Check if the state has changed, if it has, then post a user event to
            # the queue to force the menu to be shown at least once

            #pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
            
            # Get the next event
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
            
            # Update the menu, based on which "state" we are in - When using the menu
            # in a more complex program, definitely make the states global variables
            # so that you can refer to them by a name
            #if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
        '''      
                
                
            
if __name__ == "__main__":
    IntroMovie()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        