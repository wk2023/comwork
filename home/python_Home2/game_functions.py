import sys
import pygame
def check_events():
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
