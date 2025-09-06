import pygame
import constants
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid = AsteroidField()




    while True:
        screen.fill("black")
        updatable.update(dt)
        for x in drawable:
            x.draw(screen)
        pygame.display.flip()
        for x in asteroids:
            if player.collide(x):
                print("Game Over")
                return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(200)/1000


if __name__ == "__main__":
    main()
