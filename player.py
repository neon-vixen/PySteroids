import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS

class Player(CircleShape):          #<--- this is the constructor the defines the Player, what is inside the prentheses definds what it in inherits
    def __init__(self, x, y):       #< this is what is input by the player
        super().__init__(x, y, PLAYER_RADIUS)       #< this calls Circle shape constructor and fills in its parameters with what is in the Player __init__ and PLAYER_RADIUS
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", [tuple(point) for point in self.triangle()], 2)