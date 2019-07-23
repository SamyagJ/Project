import sys,pygame
from pygame.locals import *
from fish import fish

pygame.init()
screen_info = pygame.display.Info()
x=screen_info.current_w
y=screen_info.current_h

screen = pygame.display.set_mode((x,y))
clock=pygame.time.Clock()
Color=(0,1,225)

image=pygame.image.load('picture.png')
rect=image.get_rect()
rect.center=(x//2,y//2)




Bob=fish()
Bob.rect=image.get_rect()
Bob.rect.center=(x//2,y//2)
alex=fish()
alex.rect.center=(20,10)
gus=fish()
gus.rect.center=(300,200)
gus.speed=pygame.math.Vector2(2,0)


#Bob.image=pygame.image.load("picture.png")
#gus.image=pygame.image.load('picture.png')
#alex.image=pygame.image.load('picture.png')
Bob.speed=pygame.math.Vector2(0,1)


def update():
    Bob.rect.move_ip((Bob.speed))
    gus.rect.move_ip(gus.speed)

def main():
    print('Hello World')
if __name__=="__main__":
    main()

while True:
    clock.tick(60)
    screen.fill(Color)
    update()
    screen.blit(Bob.image,Bob.rect)
    screen.blit(alex.image,alex.rect)
    screen.blit(gus.image,gus.rect)
    pygame.display.flip()

import sys,pygame,random



