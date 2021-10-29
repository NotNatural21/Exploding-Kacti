import math
import pygame
#from main import SCREEN
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def zeropad(string, length):
	string = str(string)
	pad = ""
	for index in range(length - len(str)):
		pad += "0"
	return pad + string


def getLinearDistance(p1, p2):
  	return math.sqrt(((p2['x'] - p1['x']) * (p2['x'] - p1['x'])) + ((p2['y'] - p1['y']) * (p2['y'] - p1['y'])))


def degToRad(deg):
	return deg * (math.pi / 180)


def radToDeg(rad):
  	return rad * (180 / math.pi)

def between(x, min, max):
	a_bool = x >= min and x <= max
	return a_bool

def checkCollision(obj1, obj2):
	return (obj1['size'] + obj2['size']) <= getLinearDistance(obj1['pos'], obj2['pos'])


def createText(text, font_size, x, y):
	myfont = pygame.font.SysFont('Courier New', font_size)
	textsurface = myfont.render(text, False, (0, 0, 0))
	SCREEN.blit(textsurface,(x,y))