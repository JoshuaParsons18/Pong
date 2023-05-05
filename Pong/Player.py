import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, xPos=50, yPos=400, width=10, height=50, speed=250, color=(0, 0, 255)):
        super().__init__()
        
        # Dynamic attrbiutes
        self.xPos = float(xPos)
        self.yPos = float(yPos)
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        # Static attributes
        self.screen = screen
        self.win_dimensions = self.screen.get_size()
        self.screen_height = self.win_dimensions[1]
        self.score = 0
        self.isCollided = False
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)
        self.radius = max(self.width, self.height) / 2



    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


    def update(self, dt):
        # Check if out of bounds
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height


    def input_handler(self, keys, dt):
        dt = dt / 1000  # Convert milliseconds to seconds

        if keys[pygame.K_w]:
            self.rect.y -= int(self.speed * dt)
        elif keys[pygame.K_s]:
            self.rect.y += int(self.speed * dt)

