import pygame


class Static:
    def __init__(self, screen, player, levels, reset):
        self.screen = screen
        self.health = player.health
        self.maxhealth = player.maxhealth
        self.player = player
        self.maxhealth_procent = self.maxhealth / 100
        self.levels = levels
        self.reset = reset

    def update(self):
        pygame.draw.rect(self.screen, (22, 15, 14), pygame.Rect(0, 0, 800, 80))
        self.health = self.player.health
        if self.health <= 0:
            self.reset()
            self.levels()
        self.health_bar()

    def health_bar(self):
        pygame.draw.rect(self.screen, (234, 55, 21), pygame.Rect(670, 20, self.health / self.maxhealth_procent, 15))
        # pygame.draw.rect(self.screen, (34, 36, 34), pygame.Rect(0, 0, 800, 100))
