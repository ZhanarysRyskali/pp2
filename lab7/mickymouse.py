import pygame
import sys
from datetime import datetime
import math


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

curr_time = datetime.now()
curr_sec = curr_time.second
curr_min = curr_time.minute

clock_image = pygame.transform.scale(pygame.image.load('./images/mainclock.png'), (800, 600))
sechand_image = pygame.image.load('./images/leftarm.png')
sechand_image = pygame.transform.scale(sechand_image, (32, 560))
sechand_rect = sechand_image.get_rect()
sechand_rect.center = (400, 300)
minhand_image = pygame.image.load('./images/rightarm.png')
minhand_image = pygame.transform.scale(minhand_image, (700, 500))
minhand_rect = minhand_image.get_rect()
minhand_rect.center = (400, 300)
run = True
while run:
    pygame.display.update()
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
    screen.blit(clock_image, (0, 0))
    
    rot_minhand = pygame.transform.rotate(minhand_image, -1 * (curr_min) - 160)
    rot_minhand_rect = rot_minhand.get_rect()
    rot_minhand_rect.center = minhand_rect.center
    screen.blit(rot_minhand, rot_minhand_rect)
    
    rot_sechand = pygame.transform.rotate(sechand_image, -1 * (6 * curr_sec))
    rot_sechand_rect =rot_sechand.get_rect()
    rot_sechand_rect.center = sechand_rect.center
    screen.blit(rot_sechand, rot_sechand_rect)

    curr_time = datetime.now()
    curr_sec = curr_time.second
    curr_min = curr_time.minute