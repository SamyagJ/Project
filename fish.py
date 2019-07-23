#Samyag Jhaveri
#7/23/2019
#Get.Rect
#
#This is the fish class

import pygame

class fish:

    def __init__(self):
        self.type = 'goldfish'
        self.image=pygame.image.load('picture.png')
        self.speed=pygame.math.Vector2(0,1)
        self.rect=self.image.get_rect()
        self.center=(0,0)
