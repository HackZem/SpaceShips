import sys

import pygame

from Player_gun import PGun


class ShipsPlayer:

    def __init__(self, screen, img, x, y, speed, maxhealth, gun, typeName):
        self.screen = screen
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()
        self.rect_screen = screen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.reactx = float(self.rect.x)
        self.reacty = float(self.rect.y)
        self.speed = speed
        self.mright = False
        self.mleft = False
        self.mtop = False
        self.mbottom = False
        self.type = typeName
        self.list_gun = gun
        self.gun = gun(screen, self, typeName)
        self.maxhealth = maxhealth
        self.health = maxhealth

    def update(self):
        self.screen.blit(self.img, self.rect)
        self.gun.fasten_gun(self)

        if self.mright and self.rect.right < self.rect_screen.right:
            self.reactx += self.speed
        if self.mleft and self.rect.left > self.rect_screen.left:
            self.reactx -= self.speed
        if self.mbottom and self.rect.bottom < self.rect_screen.bottom - 3:
            self.reacty += self.speed
        if self.mtop and self.rect.top > self.rect_screen.top + 660:
            self.reacty -= self.speed
        self.rect.x = self.reactx
        self.rect.y = self.reacty

    def updateModule(self):
        self.gun = self.list_gun(self.screen, self, self.type)
