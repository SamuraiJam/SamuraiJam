'''
Created on Apr 4, 2012

@author: jaywaldron
'''
from samuraijam.game import *
import os
from samuraijam.game.IntroMovie import *

if __name__ == '__main__':
    #iM = IntroMovie()
    #iM.mainLoop()
    
    '''
    path = os.path.join('..','data','movie.mpg')
    os.system("open -a vlc "+path)
    '''
    #pygame.time.wait(124*10000)
    #video is 2:02 long
    
    m = MainMenu()
    m.mainLoop()