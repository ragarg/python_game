from Floor import *
from Hero import Hero
import pygame

grass_image = pygame.image.load("arts/grass.png")
dirt_image = pygame.image.load("arts/dirt.png")
hero_image = pygame.image.load("arts/hero.png")

Hero = Hero(20, 20, hero_image)
grass_maket = Floor(20, 20, grass_image)
dirt_maket = Floor(25, 27, dirt_image)
