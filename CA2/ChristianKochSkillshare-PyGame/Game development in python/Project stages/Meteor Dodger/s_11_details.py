import pygame,sys,random

class SpaceShip(pygame.sprite.Sprite):
	def __init__(self,path,x_pos,y_pos):
		super().__init__()
		self.default_ship = pygame.image.load(path)
		self.charged_ship = pygame.image.load('spaceship_charged.png')
		self.image = self.default_ship
		self.rect = self.image.get_rect(center = (x_pos,y_pos))
		self.shield_surface = pygame.image.load('shield.png')
		self.health = 5

	def update(self):
		self.rect.center = pygame.mouse.get_pos()
		self.screen_constrain()
		self.display_health()

	def screen_constrain(self):
		if self.rect.right >= 1280:
			self.rect.right = 1280
		if self.rect.left <= 0:
			self.rect.left = 0

	def display_health(self):
		for index,shield in enumerate(range(self.health)):
			screen.blit(self.shield_surface,(10 + index * 40 ,10))

	def get_damage(self,damage_amount):
		self.health -= damage_amount

	def charged(self):
		self.image = self.charged_ship

	def discharge(self):
		self.image = self.default_ship

class Meteor(pygame.sprite.Sprite):
	def __init__(self,path,x_pos,y_pos,x_speed,y_speed):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(center = (x_pos,y_pos))
		self.x_speed = x_speed
		self.y_speed = y_speed

	def update(self):
		self.rect.centerx += self.x_speed
		self.rect.centery += self.y_speed

		if self.rect.centery >= 800:
			self.kill()

class Laser(pygame.sprite.Sprite):
	def __init__(self,path,pos,speed):
		super().__init__()
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(center = pos)
		self.speed = speed

	def update(self):
		self.rect.y -= self.speed
		if self.rect.centery <= -100:
			self.kill()

def main_game():
	global laser_ready
	laser_group.draw(screen)
	spaceship_group.draw(screen)
	meteor_group.draw(screen)

	laser_group.update()
	spaceship_group.update()
	meteor_group.update()

	# Collision 
	if pygame.sprite.spritecollide(spaceship_group.sprite,meteor_group,True):
		spaceship_group.sprite.get_damage(1)

	for laser in laser_group:
		pygame.sprite.spritecollide(laser,meteor_group,True)

	# Laser charge
	if pygame.time.get_ticks() - laser_shot_time >= 1000:
		spaceship_group.sprite.charged()
		laser_ready = True


	return 1

def end_game():
	text_surface = game_font.render('Game Over',True,(255,255,255))
	text_rect = text_surface.get_rect(center = (640,340))
	screen.blit(text_surface,text_rect)

	score_surface = game_font.render(f'score: {score}',True,(255,255,255))
	score_rect = score_surface.get_rect(center = (640,380))
	screen.blit(score_surface,score_rect)
	

pygame.init() # initiate pygame
screen = pygame.display.set_mode((1280,720)) # Create display surface
clock = pygame.time.Clock() # Create clock object
game_font = pygame.font.Font('LazenbyCompSmooth.ttf', 40)
score = 0
pygame.mouse.set_visible(False)

spaceship = SpaceShip('spaceship.png', 640, 500)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

laser_group = pygame.sprite.Group()
laser_shot_time = 0
laser_ready = False

meteor_group = pygame.sprite.Group()
METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT,150)

while True: # Game loop
	for event in pygame.event.get(): # Check for events / Player input
		if event.type == pygame.QUIT: # Close the game
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and laser_ready:
			new_laser = Laser('Laser.png', event.pos, 15)
			laser_group.add(new_laser)
			spaceship_group.sprite.discharge()
			laser_shot_time = pygame.time.get_ticks()
			laser_ready = False

		if event.type == pygame.MOUSEBUTTONDOWN and spaceship_group.sprite.health <= 0:
			spaceship_group.sprite.health = 5
			score = 0

		if event.type == METEOR_EVENT:
			random_meteor_image = random.choice(('Meteor1.png','Meteor2.png','Meteor3.png'))
			random_x_pos = random.randrange(0,1280)
			random_y_pos = random.randrange(-600,-40)
			random_speed_y = random.randint(3,10)
			random_speed_x = random.randint(-1,1)
			meteor = Meteor(random_meteor_image,random_x_pos,random_y_pos,random_speed_x,random_speed_y,)
			meteor_group.add(meteor)

	screen.fill((42,45,51))
	if spaceship_group.sprite.health > 0:
		score += main_game()
	else:
		end_game()

	pygame.display.update() # Draw frame
	clock.tick(120) # Control the framerate