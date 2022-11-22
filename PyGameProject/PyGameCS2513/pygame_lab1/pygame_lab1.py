'''
Object-Oriented Version of Bouncing Ball
'''

from typing import ClassVar

import sys
import pygame
pygame.init()


class Screen:
    # __size = __width, __height = 320, 240
    # __bgcolour = 0, 0, 0  # black
    __bgcolour = ClassVar[tuple[int, int, int]]
    __size = __width, __height = ClassVar[int], ClassVar[int]

    def __init__(self, bgcolour, width, height):
        self.__bgcolour = bgcolour
        self.__width = width
        self.__height = height
        self.__size = self.__width, self.__height
        __display = pygame.display.set_mode(self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, width, height):
        self.__width = width
        self.__height = height
        self.__size = self.__width, self.__height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def bgcolour(self) -> tuple:
        return self.__bgcolour

    @bgcolour.setter
    def bgcolour(self, bgcolour: tuple):
        self.__bgcolour = bgcolour


class Ball:
    # __speed = [2, 2]  # [0] = horizontal speed, [1] = vertical speed
    __speed = ClassVar[list[int, int]]
    # __ball = pygame.image.load("intro_ball.gif")
    __ball_img = ClassVar[str]  # to operate upon file give and load file
    __image_file_name = ClassVar[str]  # to display file name

    def __init__(self, speed, image_file_name):
        self.__speed = speed
        self.__image_file_name = image_file_name
        self.__ball_img = pygame.image.load(image_file_name)
        self.__ballrect = self.__ball_img.get_rect()

    @property
    def speed(self) -> list:
        return self.__speed

    @speed.setter
    def speed(self, speed: list):
        self.__speed = speed

    @property
    def ball_img(self):
        return self.__ball_img # retrive variable that displays the image file

    @ball_img.setter
    def ball_img(self, image_file_name: str):
        self.__ball_img = pygame.image.load(image_file_name)  # set a new image for the ball

    def ballrect(self):
        return self.__ballrect


class GameSetup:
    # __game_ball = type(Ball)
    # __game_screen = type(Screen)

    def __init__(self, ball_speed, ball_image_file_name, screen_colour, screen_width, screen_height):
        self.__game_ball = Ball(ball_speed, ball_image_file_name)
        self.__ballrect = self.__game_ball.ball_img.get_rect()
        self.__game_screen = Screen(screen_colour, screen_width, screen_height)
        self.__display = pygame.display.set_mode(self.__game_screen.size)
        self.start()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.__ballrect = self.__ballrect.move(self.__game_ball.speed)
            if self.__ballrect.left < 0 or self.__ballrect.right > self.__game_screen.width:
                self.__game_ball.speed[0] = -self.__game_ball.speed[0]

            if self.__ballrect.top < 0 or self.__ballrect.bottom > self.__game_screen.height:
                self.__game_ball.speed[1] = -self.__game_ball.speed[1]

            self.__display.fill(self.__game_screen.bgcolour)
            self.__display.blit(self.__game_ball.ball_img, self.__ballrect)
            pygame.display.flip()


if __name__ == '__main__':
    run = GameSetup([3, 3], "intro_ball.gif", (0, 0, 0), 320, 240)

