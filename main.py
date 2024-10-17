import pygame
from player import Player
from constants import *

def main():
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.color.Color(0, 0, 0))
        player.draw(screen)
        pygame.display.flip()

        # 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()