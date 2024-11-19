
from Player_gun import PGun


def Guns(screen, player, species):
    if species == "laser":
        return PGun("IMG/laser.png", screen, player.rect.centerx, player.rect.top, player, 500, 12.5)
    elif species == "laser_speed":
        return PGun("IMG/laser_speed.png", screen, player.rect.centerx, player.rect.top, player, 400, 13.8)
