import pygame


class BulletEnemy(pygame.sprite.Sprite):
    def __init__(self, img, screen, player, speed, damage, x, y):
        super(BulletEnemy, self).__init__()
        self.screen = screen
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()
        self.speed = speed
        self.x = x
        self.y = y
        self.rect.centerx = self.x
        self.rect.top = self.y
        self.ry = float(self.rect.y)
        self.damage = damage
        self.player = player

    def update(self):
        self.screen.blit(self.img, self.rect)
        self.ry += self.speed
        self.rect.y = self.ry

        if self.rect.colliderect(self.player):
            self.player.health -= self.damage
            self.kill()

    def Kill(self):
        self.kill()
