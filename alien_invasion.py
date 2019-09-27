import pygame
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship


def run_game():
    # Starting game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Making a group to store the bullets in.
    bullets = Group()
    # Making of an alien in a group
    aliens = Group()

    # Make a ship
    ship = Ship(ai_settings, screen)

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create an instance to store game stats.
    stats = GameStats(ai_settings)

    # Making the play Button
    play_button = Button(screen, "Play")

    # Making scoreboard
    sb = Scoreboard(ai_settings, screen, stats)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
