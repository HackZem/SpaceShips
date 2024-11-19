import sys
import time

import pygame

from Button import Button
from OpenTxtFunctions import *
from Player_gun import PGun

shop_menu = True
message = ""

guns = {
    1: {
        "img": pygame.transform.scale(pygame.image.load("IMG/laser.png"), (70, 130)),
        "name": "laser",
        "price": 0,
        "isBuy": True,
        "active": True

    },
    2: {
        "img": pygame.transform.scale(pygame.image.load("IMG/laser_speed.png"), (70, 130)),
        "name": "laser_speed",
        "price": 75,
        "isBuy": False,
        "active": False
    }
}

number_gun = 1

isRight = False
isLeft = False


def shop(levels, player):
    global shop_menu, message
    shop_menu = True
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Космический бой")
    bg_color = (76, 128, 141)
    home_button = Button(screen, (67, 68, 69), 105, 45, 645, 25, levels, "Levels", None, (182, 189, 191), "default",
                         True)
    button_left = Button(screen, (100, 103, 84), 35, 100, 115, 280, left, "<", None, (0, 0, 0), "default",
                         True)
    button_right = Button(screen, (100, 103, 84), 35, 100, 320, 280, right, ">", None, (0, 0, 0), "default",
                          True)

    button_buy = Button(screen, (78, 193, 32), 120, 35, 175, 400, buy, message, None, (0, 0, 0), "default",
                        True)

    while shop_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        font = pygame.font.SysFont("arial", 40)
        text_money = font.render("Money:" + openTxt("upgrade_sts")["money"], True, (0, 0, 0))
        screen.blit(text_money, (30, 30))
        screen.blit(guns[number_gun]["img"], (200, 250))

        button_right.update()
        button_left.update()
        home_button.update()
        updateBuy(button_buy)
        pygame.display.flip()
        for x in range(len(guns)):
            if guns[x + 1]["active"]:
                player.type = guns[x + 1]["name"]
                player.updateModule()
                break


def right():
    global number_gun, isRight
    if not isRight:
        if number_gun < len(guns):
            isRight = True
            time.sleep(0.1)
            number_gun += 1
            isRight = False


def left():
    global number_gun, isLeft
    if not isLeft and number_gun > 1:
        isLeft = True
        time.sleep(0.1)
        number_gun -= 1
        isLeft = False


def updateBuy(button):
    global message
    button.message = message
    button.update()
    if not guns[number_gun]["isBuy"]:
        message = str(guns[number_gun]["price"])
    elif not guns[number_gun]["active"]:
        message = "Вибрать"
    else:
        message = "Вибрано"


def buy():
    global message, guns
    local_money = openTxt("upgrade_sts")
    if not guns[number_gun]["isBuy"] and guns[number_gun]["price"] <= int(local_money["money"]):
        money = int(local_money["money"])
        money -= guns[number_gun]["price"]
        local_money["money"] = str(money)
        writeTxt("upgrade_sts", local_money)
        guns[number_gun]["isBuy"] = True
    elif guns[number_gun]["isBuy"] and not guns[number_gun]["active"]:
        guns[number_gun]["active"] = True
        for x in range(len(guns)):
            if guns[x + 1] == guns[number_gun]:
                continue
            guns[x + 1]["active"] = False
