'''
Created on Apr 4, 2012

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

class MainMenu:
    def __init__(self,screen=None):
        """Initialize PyGame"""
        pygame.init()
        
        """Joystick"""
        #self.joy=pygame.joystick.Joystick(0)
        #self.joy.init()
        #self.numbutton = self.joy.get_numbuttons()
        self.screen = screen
        # Load two sounds
        #self.fluteMusic = pygame.mixer.Sound("../data/introFlute.ogg")
        #self.fluteMusic = load_sound("introFlute.ogg")
        Constants.fluteMusic = load_sound("introFlute.ogg")
        self.clashingSwords = load_sound("swords_1Clash.ogg")
        #jab = pygame.mixer.Sound("../../data/jab.ogg")
        # Play the sounds; these will play simultaneously
        Constants.fluteMusic.play()
        
    def mainLoop(self):
        # Initialize the mixer
        pygame.mixer.init()
        
        #pygame.mixer.music.load("../../data/introFlute.ogg")
        #pygame.mixer.music.play(0, 0.0)
        screen = self.screen
        """Create the Screen"""
        if screen==None:
            screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        #self.mainScreenBackground, self.mainScreenBackgroundRect = load_image("SamuraiJam_MainScreen.jpg")
        mainScreenBackground,mainScreenBackgroundRect = load_image("SamuraiJam_MainScreen.jpg")
        #mainScreenBackgroundRect = mainScreenBackground.get_rect()
        #blit once first to avoid graphics conflicts with the menu
        screen.blit(mainScreenBackground, mainScreenBackgroundRect)
        
        
        
        
        '''Create the menu'''
        # Create 3 diffrent menus.  One of them is only text, another one is only
        # images, and a third is -gasp- a mix of images and text buttons!  To
        # understand the input factors, see the menu file
        menu = cMenu(50, 50, 20, 5, 'vertical', 100, screen,
               [('Level Select', 1, None),
                ('Load Game',  2, None),
                ('Options',    3, None),
                ('Exit',       4, None)])
        #set the unselected color for menu items
        menu.set_unselected_color(BLACK)
        
        # Center the menu on the draw_surface (the entire screen here)
        menu.set_center(False, False)
    
        # Center the menu on the draw_surface (the entire screen here)
        #menu.set_alignment('center', 'center')
        menu.set_position(800,200)
        
        # Create the state variables (make them different so that the user event is
        # triggered at the start of the "while 1" loop so that the initial display
        # does not wait for user input)
        state = 0
        prev_state = 1
        
        # rect_list is the list of pygame.Rect's that will tell pygame where to
        # update the screen (there is no point in updating the entire screen if only
        # a small portion of it changed!)
        rect_list = []
        
        # Ignore mouse motion (greatly reduces resources when not needed)
        pygame.event.set_blocked(pygame.MOUSEMOTION)
    
        
        # The main while loop
        while 1:
            # Check if the state has changed, if it has, then post a user event to
            # the queue to force the menu to be shown at least once
            if prev_state != state:
                pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
                prev_state = state
            
            # Get the next event
            e = pygame.event.wait()
            
            # Update the menu, based on which "state" we are in - When using the menu
            # in a more complex program, definitely make the states global variables
            # so that you can refer to them by a name
            if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
                if state == 0:
                    rect_list, state = menu.update(e, state)
                elif state == 1:
                    print 'Start Game!'
                    self.clashingSwords.play()
                    #go to the next menu (level selection)
                    lvl = LevelSelectMenu(screen)
                    lvl.mainLoop()
                    print "outside levelSelect"
                    state = 0
                elif state == 2:
                    print 'Load Game!'
                    self.clashingSwords.play()
                    state = 0
                elif state == 3:
                    print 'Options!'
                    self.clashingSwords.play()
                    state = 0
                else:
                    print 'Exit!'
                    self.clashingSwords.play()
                    time.sleep(.5)
                    pygame.quit()
                    sys.exit()
                    
                #blit all
                pygame.display.update(rect_list)
                screen.blit(mainScreenBackground, mainScreenBackgroundRect)
                
                #pygame.display.flip()
            # Update the screen
            
            #screen.blit(rect_list)
                
                
            
if __name__ == "__main__":
    MainMenu()
    