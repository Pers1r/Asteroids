from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_SPEED, PLAYER_SHOT_COOLDOWN
import pygame
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
                self.timer = PLAYER_SHOT_COOLDOWN
        if self.timer > 0:
            self.timer -= dt

    def move(self, dt):
        vector = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += vector * PLAYER_SPEED * dt

    def shoot(self):
        vect = pygame.Vector2(0, 1).rotate(self.rotation)
        vect *= SHOT_SPEED

        shot = Shot(self.position, self.position)
        shot.velocity += vect

