import random

import pygame

from Enemies.Enemy_fighter.Enemy_fighter import Enemy_fighter
from Enemies.Enemy_satell.Enemy_satell import Enemy_satell
from Enemies.Enemy_cruise.Enemy_cruise import Enemy_cruise


def Enemy(screen, x, y, player, species, bullets):
    if species == "satell":
        return Enemy_satell("IMG/Ship_1_enemy.png", screen, 2.5, 30, x, y, 150, random.randint(60, 300), player,
                            bullets, 2)
    elif species == "fighter":
        return Enemy_fighter("IMG/enemy_fighter.png", screen, 3.1, 80, x, y, 160, random.randint(80, 280), player,
                            bullets, 10)
    elif species == "cruise":
        return Enemy_cruise("IMG/cruise.png", screen, 3.9, 120, x, y, 115, 80, 7, player,
                            bullets, 2)
    if species == "satell-boss":
        return Enemy_satell("IMG/satell_boss.png", screen, 2.1, 30, x, y, 150, random.randint(60, 300), player,
                            bullets, 2)
