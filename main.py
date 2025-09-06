import pygame
import constants
import shot
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid = AsteroidField()




    while True:
        screen.fill("black")
        updatable.update(dt)
        for x in drawable:
            x.draw(screen)
        pygame.display.flip()
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game Over")
                return
            for shot in shots:
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(200)/1000


if __name__ == "__main__":
    main()
