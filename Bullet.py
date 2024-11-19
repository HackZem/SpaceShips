import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, img, screen, enemies, speed, x, y, damage):
        super(Bullet, self).__init__()
        self.screen = screen
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()
        self.speed = speed
        self.x = x
        self.y = y
        self.rect.centerx = self.x
        self.rect.top = self.y
        self.ry = float(self.rect.y)
        self.enemies = enemies
        self.damage = damage


    def update(self):
        self.screen.blit(self.img, self.rect)
        self.ry -= self.speed
        self.rect.y = self.ry

        for enemy in self.enemies:
            if self.rect.colliderect(enemy):
                enemy.health -= self.damage
                self.kill()


    def Kill(self):
        self.kill()
