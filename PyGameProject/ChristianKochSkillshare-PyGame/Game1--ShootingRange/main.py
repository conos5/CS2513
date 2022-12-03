import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

wood_bg = pygame.image.load('GameAssets/Wood_BG.png')
land_bg = pygame.image.load('GameAssets/Land_BG.png')

while True:  # _speed of update i.e frame rate is not set!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(wood_bg, (0, 0))  # (0, 0) = top left !
    screen.blit(land_bg, (0, 560))
    pygame.display.update()
    clock.tick(120)  # stops framerate from exceeding 120 FPS