import pygame

WIDTH, HEIGHT = 900, 500  # good convention to name constant values in capitals
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    run = True
    while run:
        for event in pygame.event.get():
            
