import sys, pygame


class MyGame(object):

    def __init__(self):
        
        pygame.init()
        
        self._size = self._width, self._height = 400, 600
        self._black = 0, 0, 0
        
        self._screen = pygame.display.set_mode(self._size)

        self._ballview = pygame.image.load("pygame_ca2/graphics/player.png")
        self._ballmodel = BallState(160, 560, self._width, 3)

        self._missileList = []

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

                    if event.key == pygame.K_SPACE:
                        missile = Missile(self._ballmodel.getXPos())
                        self._missileList.append(missile)

                if event.type == pygame.KEYUP:
                    self._ballmodel.handleStopMove()
            
            self._screen.fill(self._black)
            self._screen.blit(self._ballview, (self._ballmodel.getXPos(), self._ballmodel.getYPos()))
            
            i = 0
            while i < len(self._missileList):
                self._missileList[i].moveMissile()
                self._screen.blit(self._missileList[i].getIcon(), (self._missileList[i].getXPos(), self._missileList[i].getYPos()))
                i += 1
            # print(len(self._missileList))
            pygame.display.flip()

class Missile(object):
    def __init__(self, xpos):
        self._xPos = xpos
        self._yPos = 535
        self._icon = pygame.image.load("pygame_ca2/graphics/pixel_laser_green.png")
        self._ballchange = 1

    def getXPos(self):
        return self._xPos

    def getYPos(self):
        return self._yPos

    def moveMissile(self):
            self._yPos -= self._ballchange

    def getIcon(self):
        return self._icon

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

    def handleMoveRight(self):
        
        if self._xPos + self._ballchange < self._maxXPos:
            self._xPos += self._ballchange

    def handleMoveLeft(self):
       
        if self._xPos - self._ballchange > 0:
            self._xPos -= self._ballchange

    def handleStopMove(self):
        
        self._xPos = self._xPos

if __name__ == "__main__":
    mygame = MyGame()
    mygame.rungame()
