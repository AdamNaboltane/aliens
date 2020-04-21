import sys
import pygame
from parametres import Parametres  
from vaisseau import Vaisseau
from bullet import Bullet 
from pygame.sprite import Sprite
from alien import Alien  
from time import sleep 
from stats import Stats 
from bouton import Bouton 
from scoreboard import Scoreboard



class Invaders: 

	def __init__(self):
		"""Initialisation"""
		pygame.init()
		self.parametres = Parametres()
		self.ecran = pygame.display.set_mode((self.parametres.largeur, self.parametres.hauteur)) #Créer une fenêtre 
		pygame.display.set_caption("Invaders") 
		self.stats = Stats(self)
		self.scoreboard = Scoreboard(self)

		"""Jeu en plein écran
		self.ecran = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.parametres.largeur = self.ecran.get_rect().width
		self.parametres.largeur = self.ecran.get_rect().height"""

		self.vaisseau = Vaisseau(self)
		self.bullets = pygame.sprite.Group()

		self.aliens = pygame.sprite.Group()
		self._create_fleet()
		self.play_bouton = Bouton(self, "Play")


	def run_game(self):
		while True: 
			self._check_events()
			if self.stats.game_active:
				self.vaisseau.update()
				self._update_bullets()
				self._update_aliens()
			self._update_ecran()

	def _update_aliens(self):
		self._check_fleet_edges()
		self.aliens.update()

		if pygame.sprite.spritecollideany(self.vaisseau, self.aliens):
			self._impact()

		self._check_aliens_bottom()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

	def _check_play_button(self, mouse_pos):

		button_clicked = self.play_bouton.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			self.parametres.initialize_dynamic_settings()
			self.stats.reset_stats()
			self.stats.game_active = True
			self.scoreboard.prep_score()

			self.aliens.empty()
			self.bullets.empty()

			self._create_fleet()
			self.vaisseau.centrer_vaisseau() 

			pygame.mouse.set_visible(False)


	def _check_keydown(self, event):
		if event.key == pygame.K_RIGHT:
			self.vaisseau.mouvement_droite = True 
		elif event.key == pygame.K_LEFT:
			self.vaisseau.mouvement_gauche = True
		elif event.key == pygame.K_a: #Il faut appuyer sur Q si clavier AZERTY
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup(self, event):
		if event.key == pygame.K_RIGHT:
			self.vaisseau.mouvement_droite = False
		elif event.key == pygame.K_LEFT:
			self.vaisseau.mouvement_gauche = False  		

	def _update_bullets(self):

		for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)
				#print(len(self.bullets))


		self._check_bullet_alien_collision()

		self.bullets.update()

	def _check_bullet_alien_collision(self):
		
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True) # True True : Supprimer balles et aliens 

		if collisions: 
			for aliens in collisions.values():
				self.stats.score += self.parametres.score_alien
			self.scoreboard.prep_score()
			self.scoreboard.check_high_score()

		if not self.aliens: 
			self.bullets.empty()
			self._create_fleet()
			self.parametres.inicrease_speed()

	def _update_ecran(self):
		self.ecran.fill(self.parametres.fond)		
		self.vaisseau.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.ecran)
		self.scoreboard.show_score()
		if not self.stats.game_active:
			self.play_bouton.draw_bouton()
		pygame.display.flip() #Laisser flip à la fin pour update l'écran en dernier !

	def _create_fleet(self):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size 
		available_space_x = self.parametres.largeur - (2 * alien_width)
		number_aliens_x = available_space_x // (2*alien_width)

		hauteur_vaisseau = self.vaisseau.rect.height
		available_space_y = (self.parametres.hauteur - (3 * alien_height) - hauteur_vaisseau)
		nb_lignes = available_space_y // (2*alien_height)

		for row_number in range(nb_lignes):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)

	def _create_alien(self, nb_aliens, nb_lignes):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2* alien_width * nb_aliens
		alien.rect.x = alien.x 
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * nb_lignes
		self.aliens.add(alien)

	def _fire_bullet(self):
		if len(self.bullets) < self.parametres.balles_max:
			new_Bullet = Bullet(self)
			self.bullets.add(new_Bullet)
		
	def _check_fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien.check_bords():
				self._change_direction()
				break

	def _change_direction(self):
		for alien in self.aliens.sprites():
			alien.rect.y += self.parametres.flotte_vitesse
		self.parametres.flotte_direction *= -1 

	def _impact(self):
		if self.stats.vies > 0:
			self.stats.vies -= 1
			self.aliens.empty()
			self.bullets.empty()
			self._create_fleet()
			self.vaisseau.centrer_vaisseau()
		else:
			self.stats.game_active = False 
			pygame.mouse.set_visible(True)

		sleep(0.5)

	def _check_aliens_bottom(self):
		ecran_rect = self.ecran.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= ecran_rect.bottom:
				self._impact()


if __name__ == '__main__':
	jeu = Invaders()
	jeu.run_game()