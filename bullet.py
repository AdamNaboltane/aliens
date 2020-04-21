import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, jeu):
        super().__init__()
        self.ecran = jeu.ecran
        self.parametres = jeu.parametres
        self.couleur = self.parametres.balle_couleur 

        self.rect = pygame.Rect(0,0, self.parametres.balle_largeur, self.parametres.balle_hauteur)#Permet de créer un rect from scratch
        self.rect.midtop = jeu.vaisseau.rect.midtop 

        self.y = float(self.rect.y)


    def update(self):
        self.y -=self.parametres.balle_vitesse
        self.rect.y = self.y


    def draw_bullet(self):
        pygame.draw.rect(self.ecran, self.couleur, self.rect)
        
