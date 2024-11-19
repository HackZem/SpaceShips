import random
import sys
import pygame
from Bullet import Bullet
from ListEnemies import Enemy


def events(ships, bullets, enemies, pause):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ships.mright = True
            elif event.key == pygame.K_a:
                ships.mleft = True
            elif event.key == pygame.K_s:
                ships.mbottom = True
            elif event.key == pygame.K_w:
                ships.mtop = True
            elif event.key == pygame.K_ESCAPE:
                pause()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ships.gun.shoot(enemies, bullets)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ships.mright = False
            elif event.key == pygame.K_a:
                ships.mleft = False
            elif event.key == pygame.K_s:
                ships.mbottom = False
            elif event.key == pygame.K_w:
                ships.mtop = False


