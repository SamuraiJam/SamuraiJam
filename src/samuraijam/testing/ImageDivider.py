import sys,os
import pygame
from pygame.base import *

pygame.init()

def load_image(name, colorkey=None):
    #fullname = os.path.join("..","..","..","..","..","..","Desktop",name)
    fullname = name
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
    return image, image.get_rect(), colorkey


# go through all files in a directory
dict = {(0,0,0):[]}
#cutDownPath = 
path = os.path.join("..","..","..","..","..","..","Desktop","Resized")
fileList = os.listdir(path)
for eachFile in fileList:
    pathOld = os.path.join(path,eachFile)
    
    image,rect,colorkey = load_image(pathOld,-1)
    if colorkey in dict:
        temp = dict[colorkey]
        temp.append(pathOld)
        dict[colorkey] = temp
    else:
        dict[colorkey] = [pathOld]
    

print dict

#create an image object & save the colorkey of it
    
#move corresponding file based on colorkey
#pathNew = os.path.join(newFile,eachFile)
    