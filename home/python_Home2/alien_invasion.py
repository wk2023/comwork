from settings import Settings
from ship import Ship
import game_functions as gf
import pygame
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen)
    bg_color = (230,230,230)
    while True:
        gf.check_events()
        #screen.fill(bg_color)
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()
run_game()
