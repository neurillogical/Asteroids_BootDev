import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        split_velocity_a1 = self.velocity.rotate(split_angle)
        split_velocity_a2 = self.velocity.rotate(split_angle * -1)
        split_radius = self.radius - ASTEROID_MIN_RADIUS

        new_split_asteroid_1 = Asteroid(self.position.x, self.position.y, split_radius)
        new_split_asteroid_2 = Asteroid(self.position.x, self.position.y, split_radius)

        new_split_asteroid_1.velocity = split_velocity_a1 * 1.2
        new_split_asteroid_2.velocity = split_velocity_a2 * 1.2
