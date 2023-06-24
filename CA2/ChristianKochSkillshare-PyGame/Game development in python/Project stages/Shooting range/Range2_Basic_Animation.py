import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

wood_bg = pygame.image.load('Wood_BG.png')
land_bg = pygame.image.load('Land_BG.png')
water_bg = pygame.image.load('Water_BG.png')
cloud1 = pygame.image.load('Cloud1.png')
cloud2 = pygame.image.load('Cloud2.png')

land_position_y = 560
land_speed = 1

water_position_y = 640
water_speed = 1.5

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.blit(wood_bg,(0,0))
	land_position_y -= land_speed

	if land_position_y <= 520 or land_position_y >= 600:
		land_speed *= -1
	screen.blit(land_bg,(0,land_position_y))

	water_position_y += water_speed
	if water_position_y <= 620 or water_position_y >= 680:
		water_speed *= -1
	screen.blit(water_bg,(0,water_position_y))

	screen.blit(cloud1,(100,50))
	screen.blit(cloud2,(170,80))

	screen.blit(cloud1,(604,10))
	screen.blit(cloud2,(1000,90))
	screen.blit(cloud1,(412,55))
	pygame.display.update()
	clock.tick(120)