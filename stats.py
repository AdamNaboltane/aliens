class Stats:
    def __init__(self, jeu):
        self.parametres = jeu.parametres 
        self.game_active = False
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):
        self.vies = self.parametres.viesMax 
        self.score = 0
        self.level = 1