import pygame
from Game import Game
from Settings import *

class Launcher():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.Font(None, 36)
        pygame.display.set_caption("Pong")

        game = Game(self.screen, self.font)

        self.running = True
        
        while(self.running):
            game.run()



# check if the current module is being executed as the main program
if __name__ == "__main__":
    launcher = Launcher()