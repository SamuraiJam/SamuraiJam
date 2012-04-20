'''
Created on Apr 19, 2012

@author: jaywaldron
'''
import pyganim
import sys,os
import pygame
from pygame.locals import *

pygame.init()
surface = pygame.display.set_mode((1100, 600))

def load_image(name, colorkey=None):
    fullname = os.path.join('..','..','..', 'data', name)
    #fullname = os.path.join('..', 'data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()

def getPlayerSprite(fileName):
    #return os.path.join("..","..","..","data","samurai_sprites", fileName)
    fullname = os.path.join('samurai_sprites', fileName)
    img, rect = load_image(fullname,-1)
    return img
    

def getWeaponSprite(fileName):
    return os.path.join("..","..","..","data","weapon_sprites", fileName)

def loadFiles(dirName):
    playerAnimationArray = []
    path = os.path.join("..","..","..","data",dirName)
    fileList = os.listdir(path)
    for eachFile in fileList:
        playerAnimationArray.append((getPlayerSprite(eachFile), 0.15)) #what to append & what speed it takes up in the cycle (in seconds)
    return pyganim.PygAnimation(playerAnimationArray)
#animObjPlayer = pyganim.PygAnimation([(getPlayerSprite('chr06000.BMP'), 0.2), (getPlayerSprite('chr06002.BMP'), 0.2), (getPlayerSprite('chr06004.BMP'), .4)])


animObjPlayer = loadFiles("samurai_sprites")
#animObjWeapon = loadFiles("weapon_sprites")
animObjPlayer.play()

while True: # main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill((0,0,0))
    animObjPlayer.blit(surface, (0, 0))
    pygame.display.update()
    #print animObjPlayer.getCurrentFrame()
    
    
    