import pygame


class LevelCreate:

    def __init__(self, level_number, enemies):
        self.lvl_num = level_number
        self.enemies = enemies
        self.wave = 0

    def next_wave(self):
        self.wave += 1
