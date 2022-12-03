import sys
import pygame
pygame.init()

size = width, height = 600, 400
#_speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("pygame_lab1/intro_ball.gif")
#ballrect = ball.get_rect()

ballpos = 160
ballchange = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballchange = -1

            if event.key == pygame.K_RIGHT:
                ballchange = 1

        if event.type == pygame.KEYUP:
            ballchange = 0

    #ballrect = ballrect.move(_speed)
    #if ballrect.left < 0 or ballrect.right > width:
    #    _speed[0] = -_speed[0]
    #if ballrect.top < 0 or ballrect.bottom > height:
    #    _speed[1] = -_speed[1]

    if ballpos + ballchange > 0 and ballpos + ballchange < width - 100:
        ballpos += ballchange
        screen.fill(black)
        screen.blit(ball, (ballpos, 120))
        
    pygame.display.flip()
