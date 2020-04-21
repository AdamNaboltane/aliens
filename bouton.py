import pygame.font 

class Bouton:

    def __init__(self, jeu, msg):
        self.ecran = jeu.ecran 
        self.ecran_rect = self.ecran.get_rect()

        self.largeur, self.hauteur = 200, 50
        self.bouton_couleur = (255, 0, 0)
        self.texte_couleur = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0,0, self.largeur, self.hauteur)
        self.rect.center = self.ecran_rect.center 

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.texte_couleur, self.bouton_couleur)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center 


    def draw_bouton(self):
        self.ecran.fill(self.bouton_couleur, self.rect)
        self.ecran.blit(self.msg_image, self.msg_image_rect)
