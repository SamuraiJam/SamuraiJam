import os, sys
import pygame
from pygame.locals import *

def load_image(name, colorkey=None):
    #fullname = os.path.join('..','..','..', 'data', name)
    fullname = os.path.join('..', 'data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_samurai_image(name, colorkey=None):
    #fullname = os.path.join('..','..','..', 'data', name)
    fullname = os.path.join('..', 'data', 'samurai_sprites', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', os.path.abspath(fullname)
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_image_from_folder(foldername, filename, colorkey=None):
    fullname = os.path.join('..', 'data', foldername, filename)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', os.path.abspath(fullname)
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def load_images_from_folder(folder_name, colorkey=None):
    fullname = os.path.join('..', 'data', folder_name)
    file_list = os.listdir(fullname)
    ret = []
    for file in file_list:
        file = os.path.join(fullname, file)
        try:
            image = pygame.image.load(file)
        except pygame.error, message:
            print 'Cannot load image:', file
            raise SystemExit, message
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        if image is not None:
            ret.append((image, image.get_rect()))
    return ret

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('..', 'data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message
    return sound

def load_sound_from_folder(folder_name, file_name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('..', 'data', folder_name, file_name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message
    return sound