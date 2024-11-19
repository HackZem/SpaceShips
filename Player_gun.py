import time

import pygame

from Bullet import Bullet


class PGun:
    def __init__(self, img, screen, x, y, player, shoot_time, speed):
        self.last_time = pygame.time.get_ticks()
        self.screen = screen
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()
        self.rect_screen = screen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player = player
        self.shoot_time = shoot_time
        self.speed = speed

    def update(self):
        self.screen.blit(self.img, self.rect)

    def shoot(self, enemies, bullets):
        new_time = pygame.time.get_ticks()
        if new_time - self.last_time >= self.shoot_time:
            self.last_time = new_time
            newBullet = Bullet("IMG/laser_bullet_p.png", self.screen, enemies, self.speed, self.rect.centerx, self.rect.top, 15)
            bullets.add(newBullet)

    def fasten_gun(self, player):
        self.rect.centerx = player.rect.centerx
        self.rect.bottom = player.rect.top + 1
