'''
Created on Apr 4, 2012

@author: jaywaldron
'''
import sys, os, pygame
from pygame.locals import *
from samuraijam.util import *
from menu import *
from MainGame import *
#from menu import *
#from MainMenu import *
#from samuraijam.game import *

class LevelSelectMenu:
    def __init__(self, screen):
        """Initialize PyGame"""
        #pygame.init()
        self.screen = screen
        
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
        
        """Create the Screen"""
        #screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        #self.mainScreenBackground, self.mainScreenBackgroundRect = load_image("SamuraiJam_MainScreen.jpg")
        #mainScreenBackground = pygame.image.load("../../data/SamuraiJam_MainScreen.jpg")
        #mainScreenBackgroundRect = mainScreenBackground.get_rect()
        #blit once first to avoid graphics conflicts with the menu
        #screen.blit(mainScreenBackground, mainScreenBackgroundRect)
        screen.fill((255,255,255))
        mainScreenBackground,mainScreenBackgroundRect = load_image("samuraiFlute.jpg")
        #mainScreenBackgroundRect = mainScreenBackground.get_rect()
        #blit once first to avoid graphics conflicts with the menu
        screen.blit(mainScreenBackground, (700,0))
        
        song_dir = os.path.join('..', 'data', 'songs')
        list_of_songs = os.listdir(song_dir)
        song_file_list = []
        menu_list = [('Tutorial', 1, None)]
        i_state = 1
        
        for song in list_of_songs:
            song_filename = os.path.join(song_dir, song)
            song_file_list.append(song_filename)
            song_file = open(song_filename)
            song_title = song_file.readline().strip('\n')
            i_state = i_state + 1
            menu_list.append( (song_title, i_state, None) )
            
        i_state = i_state + 1
        menu_list.append( ('Back', i_state, None))
        
        '''Create the menu'''
        # Create 3 diffrent menus.  One of them is only text, another one is only
        # images, and a third is -gasp- a mix of images and text buttons!  To
        # understand the input factors, see the menu file
        menu = cMenu(50, 50, 20, 5, 'vertical', 100, screen, menu_list)
#               [('Tutorial', 1, None),
#                ('Level 1: Sexy And I Know It - LMFAO',  2, None),
#                ('Back', 3, None)])
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
            if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
                print "Current State: {0}".format(state)
                if state == 0:
                    rect_list, state = menu.update(e, state)
                elif state == 1:
                    print 'Tutorial'
                    self.clashingSwords.play()
                    state = 0
                    
                elif state > 1 and state < i_state:
                    self.clashingSwords.play()
                    Constants.fluteMusic.stop()
                    print song_file_list[state - 2]
                    m = MainGame(song_file_list[state - 2], screen)
                    m.game_loop()
                    screen.fill((255,255,255))
                    pygame.mixer.music.stop();
                    Constants.fluteMusic.play()
                    state = 0
#                elif state == 2:
#                    print 'Level 1!'
#                    self.clashingSwords.play()
#                    Constants.fluteMusic.stop()
#                    m = MainGame(screen)
#                    m.game_loop()
#                    screen.fill((255,255,255))
#                    #Constants.sexyMusic.stop()
#                    pygame.mixer.music.stop();
#                    Constants.fluteMusic.play()
#                    state = 0
                else:
                    print 'Back to Main Menu!'
                    self.clashingSwords.play()
                    stillSelectingLevels = False
                    
                #update the screen
                pygame.display.update(rect_list)
                screen.blit(mainScreenBackground, (700,0))
                
                
                
if __name__ == "__main__":
    LevelSelectMenu()