import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    asteroid_field = AsteroidField()
    
    Shot.containers = (shots, updateable, drawable)

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for u in updateable:
            u.update(dt)
        screen.fill(pygame.color.Color(0, 0, 0))
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        # 60 fps
        dt = clock.tick(60) / 1000

        # check for collision
        for a in asteroids:
            if player.collides(a):
                exit("Game over!")


if __name__ == "__main__":
    main()