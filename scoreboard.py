import pygame.font 

class Scoreboard:
    def __init__(self, jeu):
        self.ecran = jeu.ecran 
        self.ecran_rect = self.ecran.get_rect()
        self.parametres = jeu.parametres
        self.stats = jeu.stats
        
        self.texte_couleur = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()


    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.texte_couleur, self.parametres.fond)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.ecran_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.texte_couleur, self.parametres.fond)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.ecran_rect.right - 20 
        self.score_rect.top = 20

    def show_score(self):
        self.ecran.blit(self.score_image, self.score_rect)
        self.ecran.blit(self.high_score_image, self.high_score_rect)
        self.ecran.blit(self.level_image, self.level_rect)


    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.texte_couleur, self.parametres.fond)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10