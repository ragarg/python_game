from Floor import *
from Hero import Hero
from Poor_dog import Poor_dog
import pygame

grass_image = pygame.image.load("arts/grass.png")
dirt_image = pygame.image.load("arts/dirt.png")
hero_image = pygame.image.load("arts/hero.png")
dog_image = pygame.image.load("arts/dog.png")
warp_image = pygame.image.load("arts/warp.png")


Hero = Hero(20, 20, hero_image)
Dog1 = Poor_dog(25, 20, dog_image)
Dog2 = Poor_dog(25, 21, dog_image)
mobs = [Dog1, Dog2]
grass_maket = Floor(20, 20, grass_image)
dirt_maket = Floor(25, 27, dirt_image)
