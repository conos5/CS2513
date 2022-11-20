import pygame, sys, random

class SpaceShip(pygame.sprite.Sprite):
	def __init__(self,path,pos_x,pos_y,speed):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(center = (pos_x,pos_y))
		self.speed = speed
		self.movement = 0
		self.shields = 5
		self.shield_image = pygame.image.load('shield.png')

	def update(self):
		global game_state, game_score
		self.rect.x += self.movement
		self.health_check()

		if self.shields <= 0:
			game_state = 'Score'
			game_score = pygame.time.get_ticks()

	def health_check(self):
		for index,shield in enumerate(range(self.shields)):
			screen.blit(self.shield_image,(10 + index * 40,10))

	def damage(self):
		self.shields -= 1

	def charged_laser(self):
		self.image = pygame.image.load("ship_orange_charged.png")

	def uncharge(self):
		self.image = pygame.image.load("spaceship.png")

class Laser(pygame.sprite.Sprite):
	def __init__(self,path,pos,speed):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(center = pos)
		self.speed = speed

	def update(self):
		self.rect.y -= self.speed

class Meteor(pygame.sprite.Sprite):
	def __init__(self,path,pos_x,speed_x,speed_y):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(center = (pos_x,-100))
		self.speed_x = speed_x
		self.speed_y = speed_y

	def update(self):
		self.rect.y += self.speed_y
		self.rect.x += self.speed_x
		if self.rect.y >= 1500:
			self.kill()

def main_game():
	global laser_ready
	player.draw(screen)
	meteor_group.draw(screen)
	laser_group.draw(screen)
	
	player.update()
	meteor_group.update()
	laser_group.update()

	meteor_logic()
	collision_logic(player,meteor_group,laser_group)
	if pygame.time.get_ticks() - laser_shot >= 1000:
		laser_ready = True
		spaceship.charged_laser()

def score_screen():
	score_surface = game_font.render(f'High Score: {game_score}',True,(255,255,255))
	score_rect = score_surface.get_rect(center = (640,360))
	screen.blit(score_surface,score_rect)

def meteor_logic():
	global meteor_ready
	if meteor_ready:
		random_meteor_image = random.choice(('Meteor1.png','Meteor2.png','Meteor3.png'))
		random_x_pos = random.randrange(0,1280)
		random_speed_y = random.randint(3,10)
		random_speed_x = random.randint(-1,1)
		meteor = Meteor(random_meteor_image,random_x_pos,random_speed_x,random_speed_y)
		meteor_group.add(meteor)

		random_meteor_image = random.choice(('Meteor1.png','Meteor2.png','Meteor3.png'))
		random_x_pos = random.randrange(0,1280)
		random_speed_y = random.randint(3,10)
		random_speed_x = random.randint(-1,1)
		meteor = Meteor(random_meteor_image,random_x_pos,random_speed_x,random_speed_y)
		meteor_group.add(meteor)

		meteor_ready = False

def collision_logic(player,meteor,laser):
	if pygame.sprite.spritecollide(player.sprite,meteor,True):
		spaceship.damage()

	for l in laser:
		pygame.sprite.spritecollide(l,meteor,True)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))
game_state = 'Main'
game_score = 0
game_font = pygame.font.Font(None,80)

spaceship = SpaceShip("spaceship.png",640,600,5)
player = pygame.sprite.GroupSingle()
player.add(spaceship)

laser_group = pygame.sprite.Group()
laser_ready = True
laser_shot = 0

meteor_ready = True
meteor_group = pygame.sprite.Group()

METEOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(METEOR_EVENT,250)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				spaceship.movement += spaceship.speed
			if event.key == pygame.K_LEFT:
				spaceship.movement -= spaceship.speed

			if event.key == pygame.K_SPACE and laser_ready:
				laser_group.add(Laser('Laser.png',spaceship.rect.center,15))
				laser_ready = False
				laser_shot = pygame.time.get_ticks()
				spaceship.uncharge()
					
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				spaceship.movement-= spaceship.speed
			if event.key == pygame.K_LEFT:
				spaceship.movement += spaceship.speed
		if event.type == METEOR_EVENT:
			meteor_ready = True

	screen.fill((42,45,51))
	if game_state == 'Main':
		main_game()
	elif game_state == 'Score':
		score_screen()
	
	pygame.display.flip()
	clock.tick(120)