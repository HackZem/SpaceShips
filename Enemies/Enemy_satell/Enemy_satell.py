
import random

import pygame

from Enemies.Enemy_satell import Bullet_satell


class Enemy_satell(pygame.sprite.Sprite):
    def __init__(self, img, screen, speed, health, x, y, time_move, time_shoot, player, bullets, money):
        super(Enemy_satell, self).__init__()
        self.screen = screen
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.randy = 0
        self.randx = 0
        self.move = True
        self.clock = pygame.time.Clock()
        self.const_time_move = time_move
        self.time_move = 0
        self.const_time_shoot = time_shoot
        self.time_shoot = time_shoot
        self.health = health
        self.player = player
        self.bullets = bullets
        self.money = money

    def update(self, group, setMoney):
        if self.health <= 0:
            setMoney(self.money)
            group.remove(self)
            self.kill()
        if self.move and self.time_move <= 0:
            self.move = False
            self.randx = random.randint(10, 780)
            self.randy = random.randint(90, 550)
            self.time_move = self.const_time_move
        else:
            self.time_move -= 1

        self._Move()
        self.shoot()
        self.screen.blit(self.img, self.rect)

    def _Move(self):

        if self.rect.x > self.randx:
            self.rect.x -= self.speed
        elif self.rect.x < self.randx:
            self.rect.x += self.speed
        if self.rect.y > self.randy:
            self.rect.y -= self.speed
        elif self.rect.y < self.randy:
            self.rect.y += self.speed

        else:
            self.move = True

    def shoot(self):
        if self.time_shoot <= 0:
            self.bullets.add(
                Bullet_satell.BulletEnemy("IMG/bullet_one.png", self.screen, self.player, 10.2, 30, self.rect.centerx,
                                          self.rect.bottom))

            self.time_shoot = self.const_time_shoot
        else:
            self.time_shoot -= 1
