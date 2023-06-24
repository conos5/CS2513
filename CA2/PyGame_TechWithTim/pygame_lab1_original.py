import pygame
import sys

pygame.init()
size = width, height = 320, 240

black = 0, 0, 0
screen = pygame.display.set_mode(size)
ball = pygame.image.load("../pythonProject/intro_ball.gif")

ball_pos = 160  # x value... we're only moving horizontally
ball_change = 0  # horizontal movement change


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_change = -1  # left = -1

            if event.key == pygame.K_RIGHT:
                ball_change = 1  # right = 1

        if event.type == pygame.KEYUP:
            ball_change = 0

    if ball_pos + ball_change > 0 and ball_pos + ball_change < width - ball_pos:
        ball_pos += ball_change

    screen.fill(black)
    screen.blit(ball, (ball_pos, 120))  # 120 = our y
    pygame.display.flip()
