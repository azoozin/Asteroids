# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

# ############################# #

# get new GUI window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    executing = True
    while executing:

        # Get exit button on window to work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill window with black color
        screen.fill((0, 0, 0)) # fill() receives tuple

        # Update display
        pygame.display.flip()

if __name__ == "__main__":
    main()