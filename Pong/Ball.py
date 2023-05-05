import pygame
import random
import math

class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, xPos=400, yPos=300, speed=250, color=(0,0,0), radius=10):
        super().__init__()

        # Dynamic attrbiutes
        self.xPos = xPos        # xPos = 400
        self.yPos = yPos        # yPos = 300
        self.radius = radius    # radius = 10
        self.speed = speed      # speed = 100
        self.color = color      # color = BLACK

        # Static attributes
        self.screen = screen
        self.isCollided = False
        self.angle = math.radians(random.randint(0, 360))
        self.rect = pygame.Rect(self.xPos - self.radius, self.yPos - self.radius, self.radius * 2, self.radius * 2)


    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.xPos, self.yPos), self.radius)


    def update(self, dt):
        # Move the circle by adding the speed multipled by dt
        self.xPos += int(self.speed * math.cos(self.angle) * dt / 1000)
        self.yPos += int(self.speed * math.sin(self.angle) * dt / 1000)

        self.rect = pygame.Rect(self.xPos - self.radius, self.yPos - self.radius, self.radius * 2, self.radius * 2)

        # Reset ball and angle if out of bounds
        if self.xPos - self.radius < 0 or self.xPos + self.radius > self.screen.get_width():
            self.speed = 250
            self.xPos = self.screen.get_width() // 2
            self.yPos = self.screen.get_height() // 2
            self.angle = math.radians(random.randint(45, 360))

        # Bounce ball off sides if out of bounds
        elif self.yPos - self.radius < 0:
            self.speed += 25
            # Calculate the angle of reflection based on the current angle and the position of the wall
            self.angle = -self.angle + math.radians(random.uniform(-15, 15))
            self.yPos = self.radius

        elif self.yPos + self.radius > self.screen.get_height():
            self.speed += 25
            # Calculate the angle of reflection based on the current angle and the position of the wall
            self.angle = -self.angle + math.radians(random.uniform(-15, 15))
            self.yPos = self.screen.get_height() - self.radius




