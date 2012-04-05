'''
Created on Apr 4, 2012

@author: jaywaldron
'''
import sys, os, pygame
from pygame.locals import *
from samuraijam.util import *
from menu import *
from MainMenu import *

class LevelSelectMenu(object):
    '''
    classdocs
    '''


    def __init__(self, screen):
        """Initialize PyGame"""
        #pygame.init()
        self.screen = screen
        
    def mainLoop(self):
        screen = self.screen
        """Joystick"""
        #self.joy=pygame.joystick.Joystick(0)
        #self.joy.init()
        #self.numbutton = self.joy.get_numbuttons()
        
        
        """Create the Screen"""
        #screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        #self.mainScreenBackground, self.mainScreenBackgroundRect = load_image("SamuraiJam_MainScreen.jpg")
        #mainScreenBackground = pygame.image.load("../../data/SamuraiJam_MainScreen.jpg")
        #mainScreenBackgroundRect = mainScreenBackground.get_rect()
        #blit once first to avoid graphics conflicts with the menu
        #screen.blit(mainScreenBackground, mainScreenBackgroundRect)
        screen.fill((255,255,255))
        
        
        
        
        '''Create the menu'''
        # Create 3 diffrent menus.  One of them is only text, another one is only
        # images, and a third is -gasp- a mix of images and text buttons!  To
        # understand the input factors, see the menu file
        menu = cMenu(50, 50, 20, 5, 'vertical', 100, screen,
               [('Tutorial', 1, None),
                ('Level 1: Sexy And I Know It - LMFAO',  2, None),
                ('Back', 3, None)])
        #set the unselected color for menu items
        menu.set_unselected_color(BLACK)
        
        # Center the menu on the draw_surface (the entire screen here)
        menu.set_center(False, False)

        # Center the menu on the draw_surface (the entire screen here)
        #menu.set_alignment('center', 'center')
        menu.set_position(50,50)
        
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

        stillSelectingLevels = True
        # The main while loop
        while stillSelectingLevels:
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
                    print 'Tutorial'
                    state = 0
                elif state == 2:
                    print 'Level 1!'
                    state = 0
                else:
                    print 'Back to Main Menu!'
                    #pygame.quit()
                    #sys.exit()
#                    m = MainMenu(screen)
#                    m.mainLoop()
#                    break
                    stillSelectingLevels = False
                    
                #blit all
                pygame.display.update(rect_list)
                #screen.blit(mainScreenBackground, mainScreenBackgroundRect)
            # Update the screen
            
            #screen.blit(rect_list)
            #pygame.display.flip()
        
        
    '''
    def MainLoop(self):
        # The main while loop
        while 1:
            # Check if the state has changed, if it has, then post a user event to
            # the queue to force the menu to be shown at least once
            if self.prev_state != self.state:
                pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
                self.prev_state = self.state
            
            # Get the next event
            e = pygame.event.wait()
            
            # Update the menu, based on which "state" we are in - When using the menu
            # in a more complex program, definitely make the states global variables
            # so that you can refer to them by a name
            if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
                if self.state == 0:
                    self.rect_list, state = self.menu.update(e, self.state)
                elif state == 1:
                    print 'Start Game!'
                    state = 0
                elif state == 2:
                    print 'Load Game!'
                    state = 0
                elif state == 3:
                    print 'Options!'
                    state = 0
                else:
                    print 'Exit!'
                    pygame.quit()
                    sys.exit()
                    
            #blit all
            self.screen.blit(self.mainScreenBackground, self.mainScreenBackgroundRect)
            # Update the screen
            pygame.display.update(self.rect_list)
            pygame.display.flip()
    '''
    '''       
    def MainLoop(self):
        while 1:
            for event in pygame.event.get():
                pygame.event.pump()
                m = pygame.key.get_mods()
                if m & KMOD_SHIFT:
                    sys.exit()
                
                #blit all
                self.screen.blit(self.mainScreenBackground, self.mainScreenBackgroundRect)
                pygame.display.flip()
                
    '''
                
                
                
if __name__ == "__main__":
    LevelSelectMenu()
    #MainWindow.MainLoop()
