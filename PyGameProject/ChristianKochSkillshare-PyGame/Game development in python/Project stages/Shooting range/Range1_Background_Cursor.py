import pygame, sys,random

def move_land_water():
	global water_level, land_level, water_speed, land_speed
	water_level += water_speed
	if water_level > 670 or water_level < 630:
		water_speed *= -1

	land_level += land_speed
	if land_level > 600 or land_level < 560:
		land_speed *= -1

def victory_check():
	if len(duck_list) == 0:
		message = base_font.render('You won!',True,(255,255,255))
		screen.blit(message,message.get_rect(center = (640,360)))
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))
pygame.mouse.set_visible(False)

wood_surface = pygame.image.load('Wood_BG.png')
land_surface = pygame.image.load('Land_BG.png') 
water_surface = pygame.image.load('Water_BG.png')
cloud1_surface = pygame.image.load('cloud1.png')
cloud2_surface = pygame.image.load('cloud2.png')
crosshair_surface = pygame.image.load('crosshair.png')
duck_surface = pygame.image.load('duck.png')
base_font = pygame.font.Font(None,32)

water_level = 650
water_speed = 0.8

land_level = 580
land_speed = 0.5

crosshair_posx = 0
crosshair_posy = 0

# creating ducks
duck_list = []
for duck in range(16):
	duck_x = random.randrange(50,1230)
	duck_y = random.randrange(120,600)
	new_duck = duck_surface.get_rect(center = (duck_x,duck_y))
	duck_list.append(new_duck)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEMOTION:
			crosshair_rect = crosshair_surface.get_rect(center = (event.pos[0],event.pos[1]))

		if event.type == pygame.MOUSEBUTTONDOWN:
			for index,duck in enumerate(duck_list):
				if crosshair_rect.colliderect(duck):
					del duck_list[index]


	screen.blit(wood_surface,(0,0))
	
	# spawning ducks
	for duck in duck_list:
		screen.blit(duck_surface,duck)



	screen.blit(land_surface,(0,land_level))
	move_land_water()
	screen.blit(water_surface,(0,water_level))
	screen.blit(crosshair_surface,crosshair_rect)

	screen.blit(cloud1_surface,(100,50))
	screen.blit(cloud2_surface,(170,80))

	screen.blit(cloud1_surface,(604,10))
	screen.blit(cloud2_surface,(1000,90))

	screen.blit(cloud1_surface,(412,55))
	victory_check()
	pygame.display.flip()
	clock.tick(60)