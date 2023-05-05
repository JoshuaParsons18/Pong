import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, ball, xPos=700, yPos=400, width=10, height=50, speed=275, color=(250, 0, 0)):
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
        self.ball = ball
        self.win_dimensions = self.screen.get_size()
        self.screen_height = self.win_dimensions[1]
        self.score = 0
        self.isCollided = False
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)
        self.radius = max(self.width, self.height) / 2 

    
    def update(self, dt):
        ball_Y = self.ball.yPos # Tracks y position of the ball

        # Calculate the distance between the enemy and the ball
        distance = abs(ball_Y - self.yPos)

        # Determine the movement step
        step = min(distance, self.speed * dt / 1000)

        # If ball is below enemy
        if(ball_Y > self.yPos):
            self.yPos += step
        # If ball is above enemy
        elif(ball_Y < self.yPos):
            self.yPos -= step

        # Update the rect
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)

        


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


    def TBD(self, dt):
        pass




