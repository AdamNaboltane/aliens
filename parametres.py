class Parametres:
    """Tous les paramètres sont stockés ici"""
    def __init__(self):
        #Ecran
        self.largeur = 1200
        self.hauteur = 800
        self.fond = (230, 230, 230)

        #Vaisseau
        self.viesMax = 3

        #Balles
        self.balle_largeur = 4
        self.balle_hauteur = 15
        self.balle_couleur = (255,0,0)
        self.balles_max = 3

        #Alien
        self.flotte_vitesse = 10

        #Vitesse à laquelle le jeu augmente 

        self.scale = 1.1

        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.vitesse_vaisseau = 1.5
        self.balle_vitesse = 3.0
        self.alien_vitesse = 1.0
        self.flotte_direction = 1 
        self.score_alien = 50

    def inicrease_speed(self):
        self.vitesse_vaisseau *= self.scale
        self.alien_vitesse *= self.scale 
        self.balle_vitesse *= self.scale 
        self.score_alien = int(self.score_alien * self.score_scale)

        
