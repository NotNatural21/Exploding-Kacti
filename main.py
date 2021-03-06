#Libraries
import pygame
from pygame import image
from threading import Thread
from pygame.constants import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN
pygame.font.init()
pygame.init()
#Function Files
from GAME.Settings import constants
from GAME.Settings import player
from GAME.Settings import cactus_items
from GAME.Engine import functions
from GAME.Engine import routines


#Screen and global variables
SCREEN = constants.SCREEN
MOUSE_POS = pygame.mouse.get_pos()
POND_DIM = 128
SCREEN_CENTER = constants.SCREEN_CENTER
SCREEN_HEIGHT = constants.SCREEN_HEIGHT
SCREEN_WIDTH = constants.SCREEN_WIDTH
cacti_spawn_enable = 1
pygame.display.set_caption("Exploding Kacti")

#####################################################################################
#-----------------------------------Draws the Game----------------------------------#
#####################################################################################
def draw_background():
	#Draws Background Image
	image_dim = 500
	BACKGROUND = pygame.image.load('GAME/Images/sand_background.png').convert_alpha()
	BACKGROUND = pygame.transform.scale(BACKGROUND, (image_dim, image_dim))
	for y in range(0, SCREEN_HEIGHT, image_dim):
		for x in range(0, SCREEN_WIDTH, image_dim):
			SCREEN.blit(BACKGROUND, (x, y))

def draw_game():
	#Draws pond in middle of screen
	POND = pygame.image.load('GAME/Images/ponds/pond10.png')
	POND = pygame.transform.scale(POND, (POND_DIM, POND_DIM))
	pond_offsetX = SCREEN_WIDTH / 2 - POND_DIM / 2
	pond_offsetY = SCREEN_HEIGHT / 2 - POND_DIM / 2
	SCREEN.blit(POND, (pond_offsetX, pond_offsetY))

	#Draws water meter
	bar_height = 15
	bar_width =  POND_DIM * (player.pond_item['water_amount'] / 100)
	barX = SCREEN_CENTER['x'] - POND_DIM / 2 
	barY = SCREEN_CENTER['y'] + POND_DIM / 2
	barY += bar_height
	pygame.draw.rect(SCREEN, (0, 0, 255), (barX, barY, bar_width, bar_height)) #Red Fill
	pygame.draw.rect(SCREEN, (0, 0, 0), (barX, barY, POND_DIM, bar_height), 3) #Outline
	routines.createText('Water', 15, barX + POND_DIM / 2 - 21, barY - 1) #Text
	
	#Draws health meter
	bar_height = 15
	bar_width = POND_DIM * (player.player['health'] / 100)
	barX = SCREEN_CENTER['x'] - POND_DIM / 2 
	barY = SCREEN_CENTER['y'] + POND_DIM / 2
	pygame.draw.rect(SCREEN, (255, 0, 0), (barX, barY, bar_width, bar_height)) #Red Fill
	pygame.draw.rect(SCREEN, (0, 0, 0), (barX, barY, POND_DIM, bar_height), 3) #Outline
	routines.createText('Health', 15, barX + POND_DIM / 2 - 26, barY - 1) #Text

#####################################################################################
#----------------------------------------Cacti--------------------------------------#
#####################################################################################

def spawn_cacti():
	global cacti_spawn_enable
	if len(cactus_items.all_cacti.keys()) < cactus_items.max_num_of_cacti and cacti_spawn_enable == 1:
		cacti_spawn_enable = 0
		cacti_object = routines.generateCactus()
		routines.draw_cactus(cacti_object)
		pygame.time.delay(cactus_items.cacti_spawn_rate)
		cacti_spawn_enable = 1
		

#####################################################################################
#------------------------------------Click Events-----------------------------------#
#####################################################################################

def click_events():
	if functions.checkObjectClick(POND_DIM, POND_DIM, SCREEN_CENTER['x'], SCREEN_CENTER['y']):
		routines.changeWater(50)
		


#PUT EVERYTHING BEFORE THIS
#####################################################################################
#--------------------------------------MAIN GAME------------------------------------#
#####################################################################################
#MAIN GAME

def main_menu():
	while True:
		draw_background()
		play_button = pygame.Rect(50, 100, 200, 50)
		pygame.draw.rect(SCREEN, (255, 0, 0), play_button)
		mx, my = pygame.mouse.get_pos()
		if play_button.collidepoint((mx, my)):
			game_play()
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
						pygame.quit()
		pygame.display.update()


def game_play():
	while routines.check_game_over() == False:
		pygame.time.delay(50)
		draw_background()
		draw_game()
		thread1 = Thread(target=spawn_cacti)
		thread2 = Thread(target=routines.moveAllCacti())
		thread1.start()
		thread2.start()
		
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:		
				click_events()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
						pygame.quit()
		
		pygame.display.update()
		#routines.gameOver()

main_menu()
