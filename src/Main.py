'''
Created on Apr 4, 2012

@author: jaywaldron
'''
from samuraijam.game import *
import os
from samuraijam.game.IntroMovie import *
import subprocess

if __name__ == '__main__':
    
    
    path = os.path.join('..','data','movie.mpg')
    subprocess.check_call(['/Applications/VLC.app/Contents/MacOS/VLC',path,])
    

    
    m = MainMenu()
    m.mainLoop()