import pygame
import sys
import random
import math

from Player import Player
from Enemy import Enemy
from Ball import Ball

class Game:

    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.player = Player(self.screen)
        self.ball = Ball(self.screen)
        self.enemy = Enemy(self.screen, self.ball)

        self.angle_range = random.choice([[0, 90], [270, 360]])



    def update(self, dt):
        '''responsible for updating the game state and objects on each iteration of the loop.'''
        self.draw()
        self.player.update(dt)
        self.enemy.update(dt)
        self.ball.update(dt)


    def draw(self):
        '''handles drawing to the screen. Called from game.update()'''
        # Draw objects
        self.player.draw()
        self.enemy.draw()
        self.ball.draw()

        # Draw text
        enemy_speed_text = f"{self.ball.speed}"
        text_enemy_speed = self.font.render(enemy_speed_text, True, (255, 100, 100))
        self.screen.blit(text_enemy_speed, (700, 25))


    def run(self):
        '''handles the main game loop and runs continuously until the game is exited'''
        running = True
        
        clock = pygame.time.Clock()

        while(running):
            dt = clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()

                keys = pygame.key.get_pressed()


            # Check for collisions with the player
            if pygame.sprite.collide_circle(self.player, self.ball):
                self.ball.speed *= -1
                self.ball.angle = math.radians(random.randint(self.angle_range[0], self.angle_range[1]))


            # Check for collisions with the enemy
            if pygame.sprite.collide_circle(self.enemy, self.ball):
                self.ball.speed *= -1
                self.ball.angle = math.radians(random.randint(self.angle_range[0], self.angle_range[1]))


            self.player.input_handler(keys, dt)

            self.screen.fill((0, 255, 255))
            self.update(dt)
            pygame.display.update()

        pygame.quit()