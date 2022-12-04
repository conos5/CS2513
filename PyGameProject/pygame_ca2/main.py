import pygame
import sys
import random


class Screen(object):
    def __init__(self, bg_image_file_name: str, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__size = self.__width, self.__height
        self._bg = pygame.transform.scale(pygame.image.load(bg_image_file_name), (self.width, self.height))

    # GETTERS & SETTERS
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
    def bg(self):
        return self._bg
    @property
    def bg_colour(self) -> tuple:
        return self.__bg_colour

    @bg_colour.setter
    def bg_colour(self, bg_colour: tuple):
        self.__bg_colour = bg_colour


def collide(obj1, obj2):  # -> if returns anything other than None, there is an overlap
    """
    function to determine whether object 1 & 2 collide
    :param obj1: object 1
    :param obj2: object 2
    :return: True / False on collision
    """
    offset_x = obj2.x_pos - obj1.x_pos
    offset_y = obj2.y_pos - obj1.y_pos
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y))


class Laser(object):
    def __init__(self, pos: tuple[int, int], image_file: str):
        # self._image = pygame.Surface((4, 20))  # width 4, height 20
        # self._image.fill('white')  # colour for laser
        self._x_pos = pos[0]
        self._y_pos = pos[1]

        self._image = pygame.image.load(image_file)
        self._mask = pygame.mask.from_surface(self._image)  # masks allow us to do collisions more accurately:
        #             source: "https://www.youtube.com/watch?v=uW3Fhe-Vkx4" - Understanding PyGame Masks
        # self._rect = self._image.get_rect(center=pos)

    def draw(self, window):
        """
        Draw laser function
        :param window: display/window on which to draw lasers
        :return: none
        """
        window.blit(self._image, (self._x_pos, self._y_pos))

    def movement(self, velocity: int):
        """
        laser move
        :param velocity:
        :return:
        """
        self._y_pos -= velocity

    def offscreen(self, max_y_pos):
        """
        offscreen detection function
        :param max_y_pos: maximum y position i.e. screen height
        :return: True or False
        """
        offscreen = False
        if self._y_pos >= 0 or self._y_pos <= max_y_pos:  # bullet is not within bounds...
            return offscreen
        else:  # bullet is within bounds...
            offscreen = True
            return offscreen

    def collision(self, obj):
        """
        Laser collision function
        :param obj:
        :return: True or False
        """
        return collide(obj, self)

    # GETTERS
    @property
    def x_pos(self):
        return self._x_pos

    @property
    def y_pos(self):
        return self._y_pos

    @property
    def mask(self):
        return self._mask


class Ship(object):
    def __init__(self, pos: tuple[int, int], max_x_pos: int, max_y_pos: int, blast_cooldown: int, image_file_name: str,
                 laser_image_file_name: str, sprite_change: int, sprite_health: int):
        self._pos = pos  # pos is a tuple of 2 values -> x_pos & y_pos
        self._x_pos = self._pos[0]
        self._y_pos = self._pos[1]
        self._max_x_pos = max_x_pos
        self._max_y_pos = max_y_pos

        self._change = sprite_change
        self._health = sprite_health

        self._can_shoot = True  # ready to fire, i.e reloaded
        self._blast_time = 0  # timer starts counting when laser blasted
        self._blast_cooldown = blast_cooldown  # x ms until next laser blast

        self._view = pygame.image.load(image_file_name).convert_alpha()
        self._mask = pygame.mask.from_surface(self._view)
        self._rect = self._view.get_rect(midbottom=pos)

        self._laser_image = laser_image_file_name
        self._blasts_array = []

    # def draw(self, window):
    #     window.blit(self._view, (self.x, self.y))  # draw ship
    #     for laser in self._blasts_array:  # draw laser(/s)
    #         laser.draw(window)
    #
    # def move_lasers(self, velocity, obj, ):
    #     # self.cooldown()
    #     for laser in self._blasts_array:
    #         laser.move(velocity)  # velocity will be different for enemies and players
    #         if laser.off_screen(self._max_y_pos):
    #             self._blasts_array.remove(laser)
    #         elif laser.collision(obj):
    #             obj.health -= 10
    #             self._blasts_array.remove(laser)
    # @property
    # def mask(self):
    #     return self._mask


# TODO: enemies need to be able to shoot lasers
class Enemy(Ship):
    def __init__(self, pos: tuple[int, int], max_x_pos: int, max_y_pos: int, blast_cooldown: int, image_file_name: str,
                 laser_image_file_name: str, sprite_change: dict, sprite_health: dict):
        super().__init__(pos, max_x_pos, max_y_pos, blast_cooldown, image_file_name, laser_image_file_name,
                         sprite_change, sprite_health)

    def move(self, vel):
        """
        Move enemy function
        :param vel: velocity of enemy
        :return:
        """
        self._y_pos += vel

    def draw(self, window):
        """
        Enemy draw function
        :param window: display/window upon which to draw enemy
        :return: none
        """
        window.blit(self._view, (self._x_pos, self._y_pos))

    def reloading(self):
        """
        Reload/Cooldown function
        :return: if player can shoot
        """
        if not self._can_shoot:
            current_blast_time = pygame.time.get_ticks()
            if current_blast_time - self._blast_time >= (self._blast_cooldown * 1.5):
                # if we have elapsed the x ms for our cooldown...
                self._can_shoot = True

    def blast_laser(self):
        """
        Shoot laser function
        :return: none
        """
        self._blasts_array.append(Laser((self._x_pos - 20, self._y_pos - 40), self._laser_image))

    def move_lasers(self, velocity, entities):
        """
        Moves lasers on screen
        :param velocity: speed of lasers
        :param entities: for checking collisions, namely player
        :return: none
        """
        i = 0
        while i < len(self._blasts_array):
            self._blasts_array[i].movement(velocity)
            if self._blasts_array[i].offscreen(self._max_y_pos):  # if laser goes off-screen, delete laser from array
                self._blasts_array.remove(self._blasts_array[i])
            i += 1
        for laser in self._blasts_array:
            laser.movement(velocity)  # velocity will be different for enemies and players
            if laser.offscreen(self._max_y_pos):  # if laser goes off-screen, delete laser from array
                self._blasts_array.remove(laser)
                # print(self._blasts_array())
            for entity in entities:
                if laser.collision(entity):  # if laser collides with an object, remove from array
                    entity.health -= 1
                    if laser in self._blasts_array:
                        self._blasts_array.remove(laser)
    # GETTERS
    @property
    def x_pos(self):
        return self._x_pos

    @property
    def y_pos(self):
        return self._y_pos

    @property
    def max_y_pos(self):
        return self._max_y_pos

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health_set):
        self._health = health_set

    @property
    def blasts_array(self):
        return self._blasts_array

    @property
    def view(self):
        return self._view

    @property
    def mask(self):
        return self._mask


class Player(Ship):
    def __init__(self, pos: tuple[int, int], max_x_pos: int, max_y_pos: int,
                 blast_cooldown: int, image_file_name: str, laser_image_file_name: str, sprite_change: dict,
                 sprite_health: dict):
        super().__init__(pos, max_x_pos, max_y_pos, blast_cooldown, image_file_name,
                         laser_image_file_name, sprite_change, sprite_health)
        # self._pos = pos  # pos is a tuple of 2 values -> x_pos & y_pos
        # self._x_pos = self._pos[0]
        # self._y_pos = self._pos[1]
        # self._max_x_pos = max_x_pos
        # self._max_y_pos = max_y_pos
        #
        # self._can_shoot = True  # ready to fire, i.e reloaded
        # self._blast_time = 0  # timer starts counting when laser blasted
        # self._blast_cooldown = blast_cooldown  # x ms until next laser blast
        #
        # self._view = pygame.image.load(image_file_name).convert_alpha()
        # self._mask = pygame.mask.from_surface(self._view)
        # self._rect = self._view.get_rect(midbottom=pos)
        #
        # self._laser_image = laser_image_file_name
        # self._blasts_array = []

    def user_input(self):
        """
        Function for gathering user input and hence moving player
        :return: none
        """
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_LEFT]:
            if self._x_pos > 0:
                self._x_pos -= self._change
        elif key_press[pygame.K_RIGHT]:
            if self._x_pos + 60 < self._max_x_pos:
                self._x_pos += self._change

        if key_press[pygame.K_UP] or key_press[pygame.K_SPACE]:
            if self._can_shoot:
                self.blast_laser()
                self._can_shoot = False
                self._blast_time = pygame.time.get_ticks()
                # gives us a starting time to base cooldown off
                # blast will give make laser pew noise
            else:
                # want to put sound of gun fail when not reloaded in the else
                pass

    def update(self):
        """
        update player function
        :return: none
        """
        self.user_input()
        self.reloading()

    def blast_laser(self):
        """
        Shoot laser function
        :return: none
        """
        self._blasts_array.append(Laser((self._x_pos - 20, self._y_pos - 40), self._laser_image))

    def reloading(self):
        """
        Reload/Cooldown function
        :return: if player can shoot
        """
        if not self._can_shoot:
            current_blast_time = pygame.time.get_ticks()
            if current_blast_time - self._blast_time >= self._blast_cooldown:
                # if we have elapsed the x ms for our cooldown...
                self._can_shoot = True

    def move_lasers(self, velocity, entities):
        """
        Moves lasers on screen
        :param velocity: speed of lasers
        :param entities: for checking collisions
        :return: none
        """
        i = 0
        while i < len(self._blasts_array):
            self._blasts_array[i].movement(velocity)
            if self._blasts_array[i].offscreen(self._max_y_pos):  # if laser goes off-screen, delete laser from array
                self._blasts_array.remove(self._blasts_array[i])
            i += 1
        for laser in self._blasts_array:
            laser.movement(velocity)  # velocity will be different for enemies and players
            if laser.offscreen(self._max_y_pos):  # if laser goes off-screen, delete laser from array
                self._blasts_array.remove(laser)
                # print(self._blasts_array())
            for entity in entities:
                if laser.collision(entity):  # if laser collides with an object, remove from array
                    entity.health -= 1
                    if laser in self._blasts_array:
                        self._blasts_array.remove(laser)

    # GETTERS
    @property
    def x_pos(self):
        return self._x_pos

    @property
    def y_pos(self):
        return self._y_pos

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health_set):
        self._health = health_set

    @property
    def blasts_array(self):
        return self._blasts_array

    @property
    def view(self):
        return self._view

    @property
    def mask(self):
        return self._mask

    @property
    def rect(self):
        return self._rect


# TODO: add music and sound effects for lasers, collisions and game over
class MainGame(object):
    def __init__(self, blast_cooldown: int, sprite_img_file_name: dict, laser_img_file_name: dict,
                 speed: dict, health: dict, enemy_limit: int, bg_img_file_name: str,
                 screen_width: int, screen_height: int):
        pygame.init()
        pygame.font.init()
        # Screen Setup
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._game_screen = Screen(bg_img_file_name, self._screen_width, self._screen_height)
        self._display = pygame.display.set_mode(self._game_screen.size)

        # Image Setup
        self._sprite_img_file_name = sprite_img_file_name
        self._laser_img_file_name = laser_img_file_name

        # Level Setup
        self._enemy_limit = enemy_limit
        self._enemies_array = []
        self.wave_length = 5
        self._level = 0
        self._lives = 5
        self._blast_cooldown = blast_cooldown
        self._speed = speed
        self._health = health

        # Text Setup
        self._main_font = pygame.font.SysFont("futura", 30)  # font style and size

        # Audio Setup
        self._music = pygame.mixer.Sound("audio/8-bitMusic.mp3")
        self._music.set_volume(1)
        self._music.play(loops=-1)

        # Player Instance
        self._player = Player(((self._screen_width / 2 - 20), (self._screen_height - 40)), self._screen_width,
                              self._screen_height, self._blast_cooldown, self._sprite_img_file_name["player"],
                              self._laser_img_file_name["player"], self._speed["player"], self._health["player"])

        # Clock for FPS
        self._clock = pygame.time.Clock()
        self._playing = True

    def window_draw(self, window):
        """
        Window update function
        :param window: what display/window to update
        :return: none
        """
        self._display.blit(self._game_screen.bg, (0, 0))
        # draw text
        lives_counter = self._main_font.render(f"Lives: {self._lives}", 1, (0, 255, 0))  # lives in green
        level_counter = self._main_font.render(f"Level: {self._level}", 1, (0, 0, 255))  # level in blue
        self._display.blit(lives_counter, (20, 20))
        self._display.blit(level_counter, (self._screen_width - 120, 20))

        for laser in self._player.blasts_array:  # draw laser(/s)
            laser.draw(window)

        self._player.move_lasers(self._speed["laser"], self._enemies_array)

        for enemy in self._enemies_array:
            enemy.draw(window)

        window.blit(self._player.view, (self._player.x_pos, self._player.y_pos))  # draw ship

    def run_game(self):
        """
        Main game loop with FPS to throttle
        :return: none
        """
        FPS = 60  # let's set our FPS to 60; standard FPS rate for Video Games
        while self._playing:
            self._clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.update()

            self._player.update()
            if len(self._enemies_array) == 0:
                self._level += 1
                self.wave_length += 1
                for i in range(self.wave_length):
                    rand_x = random.randrange(20, self._screen_width - 60)
                    rand_y = random.randrange(-1000, -100)
                    enemy = Enemy((rand_x, rand_y), self._screen_width, self._screen_height, self._blast_cooldown,
                                  self._sprite_img_file_name["enemy"], self._laser_img_file_name["enemy"],
                                  self._speed["enemy"], self._health["enemy"])
                    self._enemies_array.append(enemy)
            for enemy in self._enemies_array[:]:
                if enemy.health > 0:
                    enemy.move(self._speed["enemy"]+(0.2*self._level))
                    # print(len(self._enemies_array))
                    if enemy.y_pos > enemy.max_y_pos:
                        self._lives -= 1
                        # print(self._lives)
                        self._enemies_array.remove(enemy)
                        print(len(self._enemies_array))
                    elif collide(enemy, self._player):
                        self._lives -= 1
                        self._player.health -= 1
                        self._enemies_array.remove(enemy)
                else:
                    self._enemies_array.remove(enemy)
            if self._lives == 0:
                self._playing = False  # crashes game... want to make an end game screen

            self.window_draw(self._display)


if __name__ == "__main__":
    sprite_map = {
        "player": "graphics/player.png",
        "enemy": "graphics/red.png"
    }
    laser_map = {
        "player": "graphics/pixel_laser_green.png",
        "enemy": "graphics/pixel_laser_red.png"
    }
    speed_map = {
        "player": 5,
        "enemy": 0.5,
        "laser": 6
    }
    health_map = {
        "player": 5,
        "enemy": 1
    }
    mygame = MainGame(600, sprite_map, laser_map, speed_map, health_map, 5, "graphics/pixelated_space.jpg", 400, 600)
    mygame.run_game()
# TODO: make enemies shoot lasers
# TODO: end game screen
