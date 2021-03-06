import os, sys
import pygame
from samuraijam.util.Helpers import *
from pygame.locals import *
from Bar import *

class StatusBar:
    """The Main PyMan Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self, surface, color, width, height, x, y, song_name):
        self.surface = surface
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.song_title = song_name
        
        self.score = 0
        
        self.status_icons = {}
        
        #sub bars
        self.barHeight = height*.5 #factor of how large the bar is. 1 = 100%
        self.barY = (height-self.barHeight)/2
        
        self.font = pygame.font.Font(None, 26)
        
        self.hpPos = 400
        self.mpPos = 600
        self.song_title_pos = 80
        
        self.healthBar = Bar(surface=self.surface, frontColor=(255,0,0), backColor=(128,128,128), curValue=100, maxValue=100, width=150, height=self.barHeight, x=self.hpPos, y=self.barY)
        self.kiBar = Bar(surface=self.surface, frontColor=(0,0,255), backColor=(128,128,128), curValue=100, maxValue=100, width=150, height=self.barHeight, x=self.mpPos, y=self.barY)
        
        self.draw()
        self.update_score(0)    # Force draw the initial zero
        
        
    def draw(self):
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.surface, self.color, self.rect, 0)
        
        
        
        
        song_title_text = self.font.render(self.song_title, 1, (10, 10, 10))
        song_title_text_pos = song_title_text.get_rect()
        song_title_text_pos.centerx = song_title_text_pos.width / 2.0
        song_title_text_pos.centery = self.barY + song_title_text_pos.height
        self.surface.blit(song_title_text, song_title_text_pos)
        
        # Display some hpText and Bar
        
        hpText = self.font.render("HP:", 1, (10, 10, 10))
        hpTextPos = hpText.get_rect()
        hpTextPos.centerx = self.hpPos - 20
        hpTextPos.centery = self.barY+hpText.get_rect().height
        self.surface.blit(hpText, hpTextPos)
        self.healthBar.draw()

        # Display some mpText and Bar
        
        mpText = self.font.render("Ki:", 1, (10, 10, 10))
        mpTextPos = mpText.get_rect()
        mpTextPos.centerx = self.mpPos - 20
        mpTextPos.centery = self.barY+mpText.get_rect().height
        self.surface.blit(mpText, mpTextPos)
        self.kiBar.draw()
        
        
        # Display the score!
        score_pos = 800
        score_text = self.font.render("Score:", 1, (10, 10, 10))
        score_text_pos = score_text.get_rect()
        score_text_pos.centerx = score_pos - 20
        score_text_pos.centery = self.barY + score_text_pos.height
        self.surface.blit(score_text, score_text_pos)


        cur_icon_x_pos = self.width - 32
        cur_icon_y_pos = self.barY
        # Draw some status icons
        for icon in self.status_icons.values():
            
            self.surface.blit(icon, (cur_icon_x_pos, cur_icon_y_pos))
            
            cur_icon_x_pos = cur_icon_x_pos - 46

        # Display some expText and Bar
#        expPos = 800
#        expText = font.render("Rep:", 1, (10, 10, 10))
#        expTextPos = expText.get_rect()
#        expTextPos.centerx = expPos - 20
#        expTextPos.centery = self.barY+expText.get_rect().height
#        self.surface.blit(expText, expTextPos)
#        self.kiBar = Bar(surface=self.surface, frontColor=(0,255,0), backColor=(128,128,128), curValue=100, maxValue=100, width=150, height=self.barHeight, x=expPos, y=self.barY)

        
    def update_score(self, add_score):
        self.draw()
        self.score = self.score + add_score
        score_pos = 800
        score_val = self.font.render(str(self.score), 1, (10, 10, 10))
        score_val_pos = score_val.get_rect()
        score_val_pos.centerx = score_pos + 20
        score_val_pos.centery = self.barY + score_val_pos.height
        self.surface.blit(score_val, score_val_pos)
        
        
    def add_status_icon(self, icon_name):
        print "trying to add ", icon_name
        if not (icon_name in self.status_icons):
            new_icon, jank_rect = load_image_from_folder('status_icons', icon_name)
            self.status_icons[icon_name] = new_icon
            self.update_score(0)        # calls Draw
    
    def remove_status_icon(self, icon_name):
        if icon_name in self.status_icons:
            del self.status_icons[icon_name]
            self.update_score(0)       # calls Draw