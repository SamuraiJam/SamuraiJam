'''
Created on Apr 19, 2012

@author: jaywaldron
'''
import pyganim
import sys,os
import pygame
from pygame.locals import *
from samuraijam.util import *

pygame.init()
surface = pygame.display.set_mode((1100, 600))

def getPlayerSprite(fileName):
    #return os.path.join("..","..","..","data","samurai_sprites", fileName)
    fullname = os.path.join('samurai_sprites', fileName)
    img, rect = load_image(fullname,-1)
    return img
    

def getWeaponSprite(fileName):
    return os.path.join("..","..","..","data","weapon_sprites", fileName)


playerAnimationArray = []
path = os.path.join("..","..","..","data","samurai_sprites")
fileList = os.listdir(path)
for eachFile in fileList:
    playerAnimationArray.append((getPlayerSprite(eachFile), 0.2))
#animObj = pyganim.PygAnimation([(getPlayerSprite('chr06000.BMP'), 0.2), (getPlayerSprite('chr06002.BMP'), 0.2), (getPlayerSprite('chr06004.BMP'), .4)])


animObj = pyganim.PygAnimation(playerAnimationArray)
animObj.play()

while True: # main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill((0,0,0))
    animObj.blit(surface, (0, 0))
    pygame.display.update()
    print animObj.getCurrentFrame()
    
    
    