import sys

import pygame

from Button import Button
from OpenTxtFunctions import *

setting_menu = True


def setting(menu):
    global setting_menu
    setting_menu = True
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Космический бой")
    bg_color = (76, 128, 141)
    home_button = Button(screen, (67, 68, 69), 105, 45, 50, 25, menu, "Home", None, (182, 189, 191), "default",
                         True)
    reset_button = Button(screen, (219, 55, 42), 200, 45, 580, 25, reset, "Reset", None, (182, 189, 191), "default",
                          True)
    while setting_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        home_button.update()
        reset_button.update()
        pygame.display.flip()


isReset = False


def reset():
    global isReset
    if not isReset:
        isReset = True
        levels_data = openTxt("levels_sts")

        for x in range(len(levels_data) + 1):
            if x == 0 or x == 1:
                continue
            levels_data[str(x)] = False
        writeTxt("levels_sts", levels_data)
        isReset = False
