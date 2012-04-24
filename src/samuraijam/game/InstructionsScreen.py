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


class InstructionsScreen:
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
        self.winSurface.fill((0,0,0))           # this fills the entire surface
        screen.blit(self.winSurface, (0,0))    # (0,0) are the top-left coordinates
        
        
        state = 0
        prev_state = 1
        
        done = False
        while not done:
            
            if prev_state != state:
                pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
                prev_state = state

            e = pygame.event.wait()
            
            if e.type == pygame.JOYBUTTONDOWN:
                g_state = self.hal.parseButton(self.joy)
                if (HAL.GREEN in g_state and g_state[HAL.GREEN] == True):
                    e = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_RIGHT)
                elif (HAL.RED in g_state and g_state[HAL.RED] == True):
                    e = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_LEFT)
            
            if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
                if e.key == pygame.K_RIGHT:
                    state = state + 1
                elif e.key == pygame.K_LEFT:
                    state = state - 1
                        
                screen.fill((0,0,0))
                font = Font(None, 60)
                text = font.render("How to Play:", 1, (255,255,255))
                screen.blit(text, (400,50))
                font = Font(None, 40)
                text = font.render("Press GREEN to continue or RED to go back", 1, (255,255,255))
                screen.blit(text, (250, 120))
                    
                if state == 0:
                    text = font.render("This is a path that you can move on:", 1, (255,255,255))
                    screen.blit(text, (50,200))
                    image = load_image("dirtPathPanel.jpg")[0]
                    screen.blit(image, (600,200))
                    text = font.render("This is Sam:", 1, (255,255,255))
                    screen.blit(text, (50,250))
                    image = load_image("samurai_sprites/chr06164.png", -1)[0]
                    screen.blit(image, (250,250))
                    text = font.render("This is a bridge:", 1, (255,255,255))
                    screen.blit(text, (50,300))
                    image = load_image("bridges/blue_bridge.png", -1)[0]
                    screen.blit(image, (350, 270))
                    text = font.render("To cross a bridge, STRUM the guitar controller while", 1, (255,255,255))
                    screen.blit(text, (50, 350))
                    text = font.render("holding down the corresponding colored button", 1, (255,255,255))
                    screen.blit(text, (50,380))
                    text = font.render("This is a mine", 1, (255,255,255))
                    screen.blit(text, (50,430))
                    image = load_image("mine_blink/mine_1.png", -1)[0]
                    screen.blit(image, (250,430))
                    text = font.render("You want to avoid all mines.", 1, (255,255,255))
                    screen.blit(text, (50,460))
                    prev_state = 0
                elif state == 1:
                    text = font.render("ENEMIES:", 1, (255,255,255))
                    screen.blit(text, (400,170))
                    text = font.render("This is a groupie:", 1, (255,255,255))
                    screen.blit(text, (50,220))
                    image = load_image("groupie/groupie_1.png", -1)[0]
                    screen.blit(image, (350,195))
                    text = font.render("They hate being clean and are destroyed by your water attack", 1, (255,255,255))
                    screen.blit(text, (50,250))
                    text = font.render("To do your water attack: STRUM the guitar controller", 1, (255,255,255))
                    screen.blit(text, (50,280))
                    text = font.render("while holding the GREEN and BLUE buttons", 1, (255,255,255))
                    screen.blit(text, (50,310))
                    text = font.render("This is a bodyguard:", 1, (255,255,255))
                    screen.blit(text, (50,360))
                    image = load_image("guard/guard.png", -1)[0]
                    screen.blit(image, (450,335))
                    text = font.render("They are strong and need to be defeated by your fiery sword", 1, (255,255,255))
                    screen.blit(text, (50,390))
                    text = font.render("To do your fire sword attack: STRUM the guitar controller", 1, (255,255,255))
                    screen.blit(text, (50,420))
                    text = font.render("while holding the RED and YELLOW buttons", 1, (255,255,255))
                    screen.blit(text, (50,450))
                    text = font.render("This is a lawyer:", 1, (255,255,255))
                    screen.blit(text, (50,500))
                    image = load_image("lawyer/lawyer_ZZZ30.png", -1)[0]
                    screen.blit(image, (300,475))
                    text = font.render("They are very stiff and need to be mellowed by a face melting solo", 1, (255,255,255))
                    screen.blit(text, (50,530))
                    text = font.render("To do a face melting solo: STRUM the guitar controller", 1, (255,255,255))
                    screen.blit(text, (50,560))
                    text = font.render("while holding the GREEN and YELLOW buttons", 1, (255,255,255))
                    prev_state = 1
                elif state == 2:
                    text = font.render("KI:", 1, (255,255,255))
                    screen.blit(text, (400,200))
                    text = font.render("Ki is ancient spiritual energy that a Jamurai can harvest.", 1, (255,255,255))
                    screen.blit(text, (50,250))
                    text = font.render("Your Ki level is tracked in the status bar above next to your health.", 1, (255,255,255))
                    screen.blit(text, (50,290))
                    text = font.render("Using your special attacks costs Ki, but killing enemies replenishes it.", 1, (255,255,255))
                    screen.blit(text, (50,330))
                    text = font.render("Using the correct attack on an enemy will take one hit to defeat them", 1, (255,255,255))
                    screen.blit(text, (50,370))
                    text = font.render("and have no net loss of Ki. The wrong attack will still hurt enemies,", 1, (255,255,255))
                    screen.blit(text, (50,410))
                    text = font.render("but will take multiple hits to work and therefore cost Ki. You may also use", 1, (255,255,255))
                    screen.blit(text, (50,450))
                    text = font.render("your basic attack on enemies, although it is even weaker than the wrong attack.", 1, (255,255,255))
                    screen.blit(text, (50,490))
                    text = font.render("To do your basic slash attack: STRUM the guitar controller", 1, (255,255,255))
                    screen.blit(text, (50,530))
                    text = font.render("while holding the GREEN and RED buttons", 1, (255,255,255))
                    screen.blit(text, (50,570))
                    prev_state = 2
                elif state == 3:
                    text = font.render("POWERUPS:", 1, (255,255,255))
                    screen.blit(text, (400,200))
                    text = font.render("You may pick up powerups along your journey.", 1, (255,255,255))
                    screen.blit(text, (50,250))
                    text = font.render("This is a health pack:", 1, (255,255,255))
                    screen.blit(text, (50,300))
                    image = load_image("powerups/health_pack.png", -1)[0]
                    screen.blit(image, (450,300))
                    text = font.render("It increases your health as seen in the status bar.", 1, (255,255,255))
                    screen.blit(text, (50,330))
                    text = font.render("This is a Ki booster:", 1, (255,255,255))
                    screen.blit(text, (50,380))
                    image = load_image("powerups/ki_pickup.png", -1)[0]
                    screen.blit(image, (450,380))
                    text = font.render("It increases your Ki level as seen in the status bar.", 1, (255,255,255))
                    screen.blit(text, (50,410))
                    text = font.render("This is a shield:", 1, (255,255,255))
                    screen.blit(text, (50,460))
                    image = load_image("powerups/shield_pickup.png", -1)[0]
                    screen.blit(image, (450,460))
                    text = font.render("It protects you from enemies for a period of time.", 1, (255,255,255))
                    screen.blit(text, (50,490))
                    text = font.render("This is a special sword:", 1, (255,255,255))
                    screen.blit(text, (50,540))
                    image = load_image("powerups/sword_pickup.png", -1)[0]
                    screen.blit(image, (240,540))
                    text = font.render("It makes your basic slash more powerful for a period of time.", 1, (255,255,255))
                    screen.blit(text, (50,570))
                    prev_state = 3
                else:
                    done = True
                pygame.display.flip() 
        
                
if __name__ == "__main__":
    InstructionsScreen()
    
    
