import sys
import pygame


class MyGame(object):

    def __init__(self):
        
        pygame.init()
        
        self._size = self._width, self._height = 320, 240
        self._black = 0, 0, 0
        
        self._screen = pygame.display.set_mode(self._size)

        self._ballview = pygame.image.load("intro_ball.gif")
        self._ballmodel = BallState(160, 120, self._width, 3)

    def rungame(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self._ballmodel.handleMoveLeft()

                    if event.key == pygame.K_RIGHT:
                        self._ballmodel.handleMoveRight()

                if event.type == pygame.KEYUP:
                    self._ballmodel.handleStopMove()
            
            self._screen.fill(self._black)
            self._screen.blit(self._ballview, (self._ballmodel.getXPos(), self._ballmodel.getYPos()))
            pygame.display.flip()

class BallState(object):
    def __init__(self, xpos, ypos, maxxpos, change):
        self._xPos = xpos
        self._yPos = ypos
        self._maxXPos = maxxpos
        self._ballchange = change

    def getXPos(self):
        return self._xPos

    def getYPos(self):
        return self._yPos

    def handleMoveLeft(self):
        
        if self._xPos + self._ballchange < self._maxXPos:
            self._xPos -= self._ballchange

    def handleMoveRight(self):
       
        if self._xPos - self._ballchange > 0:
            self._xPos += self._ballchange

    def handleStopMove(self):
        
        self._xPos = self._xPos

if __name__ == "__main__":
    mygame = MyGame()
    mygame.rungame()