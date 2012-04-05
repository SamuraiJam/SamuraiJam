import os, sys
import pygame
from Helpers import *
from pygame.locals import *
from samuraijam import Samurai
# from Gameboard import *
from samuraijam.UI import *
from samuraijam.Enemies import *
from samuraijam.EnemySpawn import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'



class SamuraiJamMain:
    """The Main PyMan Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self, width=1100,height=600):
        self.velocity = 10
        
        """Initialize PyGame"""
        pygame.init()
        
        """Joystick"""
        #self.joy=pygame.joystick.Joystick(0)
        #self.joy.init()
        #self.numbutton = self.joy.get_numbuttons()
        
        """Set the window Size"""
        self.width = width
        self.height = height
        
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        """create the status bar"""
        statusBarHeight = int(float(height)*0.1)
        self.statusBar = StatusBar(surface=self.screen,color=(200, 200, 200),width=width,height=statusBarHeight,x=0,y=0)
        
        """Create the game field (with guitar string paths)"""
        self.boardHeight = height - statusBarHeight
        self.guitarStringPaths = [height*0.20, height*0.30, height*0.40, height*0.50, height*0.60, height*0.70]
        self.gameboard = OldGameboard(surface=self.screen, width=width, height=self.boardHeight, guitarStrings=self.guitarStringPaths)
        
        #draw background
        pygame.display.flip()
        
        
        self.clock = pygame.time.Clock()
        self.totalTime = 0
        
    def MainLoop(self):
        """This is the Main Loop of the Game"""
        """Load All of our Sprites"""
        self.LoadSprites();
        """gets data structure for spawn patterns"""
        spawnList = getSpawnList()
        
        pygame.mixer.music.load("guitar.ogg")
        pygame.mixer.music.play(0, 0.0)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == pygame.JOYBUTTONDOWN:
                    if self.joy.get_button(0)==1 or self.joy.get_button(1)==1: #strumming
                        keysPressed = [self.joy.get_button(11),self.joy.get_button(12),self.joy.get_button(14),self.joy.get_button(13),self.joy.get_button(8)]
                        if keysPressed == [1,0,0,0,0]:
                            #print "Pressed Green!"
                            #move samurai up one string
                            self.samurai.moveToHigher(0)
                        elif keysPressed == [0,0,0,0,1]:
                            #move samurai down one string
                            self.samurai_sprites.sprites()[0].moveToLower(4)
                        #elif keysPressed == [0,1,1,0,0]:
                            #basic attack?
            self.clock.tick()
            self.totalTime = self.totalTime + self.clock.get_time()
            while spawnList[0][0] <= self.totalTime:
                monster = spawnList[0][1]
                if monster[0] != 0:
                    self.enemy_sprites.add(Enemy(self.velocity,self.width,self.guitarStringPaths[0]))
                if monster[1] != 0:
                    self.enemy_sprites.add(Enemy(self.velocity,self.width,self.guitarStringPaths[1]))
                if monster[2] != 0:
                    self.enemy_sprites.add(Enemy(self.velocity,self.width,self.guitarStringPaths[2]))
                if monster[3] != 0:
                    self.enemy_sprites.add(Enemy(self.velocity,self.width,self.guitarStringPaths[3]))
                if monster[4] != 0:
                    self.enemy_sprites.add(Enemy(self.velocity,self.width,self.guitarStringPaths[4]))
                #self.enemy_sprites.add(Enemy(self.velocity,self.width,monster))
                del spawnList[0]
            #print self.clock.get_time()
            #self.screen.blit(self.gameboard, (self.width,self.boardHeight))
            #self.screen.fill([0,0,0])
            for b in self.gameboard.paths:
                #b.update(time, 150)
                self.screen.blit(b.image, b.rect)
            self.samurai_sprites.clear(self.screen,self.fillBlack)
            self.enemy_sprites.clear(self.screen,self.fillBlack)
            self.samurai_sprites.update()
            self.enemy_sprites.update()
            self.samurai_sprites.draw(self.screen)
            self.enemy_sprites.draw(self.screen)
            #self.screen.blit(self.enemy.image, self.enemy.rect.topleft)
            pygame.display.flip()
            
            #watch for collision & handle accordingly
            collided = pygame.sprite.groupcollide(self.samurai_sprites, self.enemy_sprites, False, True)
            if len(collided) > 0:
                self.statusBar.healthBar.update(-10)
                if self.statusBar.healthBar.curValue < 1:
                    sys.exit()
                    
                
                  
    def fillBlack(self,surf,rect):
        color = 0,0,0
        surf.fill(color,rect)
        
      
    def LoadSprites(self):
        """Load the sprites that we need"""
        self.samurai = Samurai(self.guitarStringPaths)
        self.samurai_sprites = pygame.sprite.RenderPlain((self.samurai))
        
        self.enemy = Enemy(self.velocity,self.width, self.guitarStringPaths[2])
        self.enemy_sprites = pygame.sprite.RenderPlain((self.enemy))
        
                    
                    
if __name__ == "__main__":
    MainWindow = SamuraiJamMain()
    MainWindow.MainLoop()