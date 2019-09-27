import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # A Class to rep a single alien in fleet.
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('alien.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact pos as a decimal
        self.x = float(self.rect.x)

    def update(self):
        # Moving the alien
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        # return true if alien hits the wall
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        # Drawing the alien at its current location.
        self.screen.blit(self.image, self.rect)
