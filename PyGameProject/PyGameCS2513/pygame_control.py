import sys, pygame
pygame.init()

size = width, height = 320, 240
#speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
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

    #ballrect = ballrect.move(speed)
    #if ballrect.left < 0 or ballrect.right > width:
    #    speed[0] = -speed[0]
    #if ballrect.top < 0 or ballrect.bottom > height:
    #    speed[1] = -speed[1]

    if ballpos + ballchange > 0 and ballpos + ballchange < width - 100:
        ballpos += ballchange
        screen.fill(black)
        screen.blit(ball, (ballpos, 120))
        
    pygame.display.flip()
