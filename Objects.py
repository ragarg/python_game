from Object import *
import pygame

grass_image = pygame.image.load("arts/grass.png")
dirt_image = pygame.image.load("arts/dirt.png")

grass_maket = Object(20, 20, grass_image)
dirt_maket = Object(25, 27, dirt_image)