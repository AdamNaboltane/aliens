import pygame 

class Vaisseau:
    def __init__(self, jeu):
    
        self.ecran = jeu.ecran
        self.ecran_rect = jeu.ecran.get_rect()

        self.parametres = jeu.parametres



        self.image = pygame.image.load('D:\Documents\Prog\Exercices python\Aliens\images\ship.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.ecran_rect.midbottom

        self.x = float(self.rect.x) #Position X du vaisseau stockée en float

        #Etat mouvement droite 
        self.mouvement_droite = False
        self.mouvement_gauche = False





    def update(self):
        if self.mouvement_droite and self.rect.right < self.ecran_rect.right:
            self.x += self.parametres.vitesse_vaisseau
        if self.mouvement_gauche and self.rect.left > 0:
            self.x -= self.parametres.vitesse_vaisseau

        self.rect.x = self.x
    
    def blitme(self):
        self.ecran.blit(self.image, self.rect)

    def centrer_vaisseau(self):
        self.rect.midbottom = self.ecran_rect.midbottom
        self.x = float(self.rect.x)

    

