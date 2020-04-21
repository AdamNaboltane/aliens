import pygame 
from pygame.sprite import Sprite 

class Alien(Sprite):


    def __init__(self, jeu):
        super().__init__()
        self.ecran = jeu.ecran 

        

        self.image = pygame.image.load('D:\Documents\Prog\Exercices python\Aliens\images\\alien.bmp')
        self.rect = self.image.get_rect()
        self.parametres = jeu.parametres 

        #Spawn l'alien en haut à gauche de l'écran 

        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height 

        self.x = float(self.rect.x)


    def check_bords(self):
        rect_ecran = self.ecran.get_rect()
        if self.rect.right >= rect_ecran.right or self.rect.left <= 0:
            return True 


    def update(self):
        self.x += (self.parametres.alien_vitesse * self.parametres.flotte_direction)
        self.rect.x = self.x 




