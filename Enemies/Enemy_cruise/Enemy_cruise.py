import random

import pygame

from Enemies.Enemy_cruise import Bullet_cruise


class Enemy_cruise(pygame.sprite.Sprite):
    def __init__(self, img, screen, speed, health, x, y, time_move, time_shoot, shoot_tick, player, bullets, money):
        super(Enemy_cruise, self).__init__()
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
        self.shoot_tick = shoot_tick
        self.const_shoot_tick = shoot_tick
        self.isShoot = False
        self.tick = 0
        self.a = -10

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
        if not self.isShoot:
            if self.time_shoot <= 0:
                self.isShoot = True
            else:
                self.time_shoot -= 1

        else:

            if self.tick < 4:
                if self.shoot_tick <= 0:
                    self.shoot_tick = self.const_shoot_tick
                    self.tick += 1
                    self.bullets.add(
                        Bullet_cruise.BulletEnemy("IMG/bullet_cruise.png", self.screen, self.player, 9.6, 20,
                                                  self.rect.centerx - self.a,
                                                  self.rect.bottom))
                    self.a = -self.a
                else:
                    self.shoot_tick -= 1
            else:
                self.time_shoot = self.const_time_shoot
                self.shoot_tick = self.const_shoot_tick
                self.isShoot = False
                self.tick = 0
