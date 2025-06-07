import circleshape
import pygame
from constants import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        a1 = self.velocity.rotate(angle)
        a2 = self.velocity.rotate(-angle)
        r = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position[0], self.position[1], r)
        ast1.velocity = a1 * 1.2
        ast2 = Asteroid(self.position[0], self.position[1], r)
        ast2.velocity = a2 * 1.2

