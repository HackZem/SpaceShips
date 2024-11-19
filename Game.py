import random
import sys
import time

import pygame_menu
import pygame
import Controls
from Button import Button
from LevelCreate import LevelCreate
from ListEnemies import Enemy
from ListGuns import Guns
from OpenTxtFunctions import *
from Setting import setting
from Shop import shop
from Statistics import Static
from UpdateScreen import UpdateSCR
from ShipsPlayer import ShipsPlayer

screen = pygame.display.set_mode((800, 800))
shipsP = ShipsPlayer(screen, "IMG/pixil-layer-0.png", 450, 750, 3.5, 100, Guns, "laser")

bullets = pygame.sprite.Group()
bullets_enemy = pygame.sprite.Group()
enemies = pygame.sprite.Group()
menu = True
run_levels = True
game = True
money = int(openTxt("upgrade_sts")["money"])
testMoney = 0
pause = False


def create_levels(scr, player, bulletsindeg):
    levels = [
        LevelCreate(1,
                    {
                        1: [Enemy(scr, random.randint(0, 780), -random.randint(10, 200), player, "satell", bulletsindeg)
                            for f in range(3)] + [Enemy(scr, random.randint(0, 780), 100, player, "cruise", bulletsindeg)],
                        2: [Enemy(scr, random.randint(0, 780), -random.randint(10, 200), player, "satell", bulletsindeg)
                            for f in range(5)]
                    }),
        LevelCreate(2,
                    {
                        1: [Enemy(scr, random.randint(0, 780), -random.randint(10, 200), player, "satell", bulletsindeg)
                            for f in range(12)]

                    }),
        LevelCreate(3,
                    {
                        1: [Enemy(scr, random.randint(0, 780), -random.randint(10, 200), player, "fighter",
                                  bulletsindeg) for f in range(1)],
                        2: [Enemy(scr, random.randint(0, 780), -random.randint(10, 200), player, "fighter",
                                  bulletsindeg),
                            Enemy(scr, random.randint(0, 780), -random.randint(10, 200), player, "fighter",
                                  bulletsindeg),
                            Enemy(scr, random.randint(0, 780), -random.randint(10, 200), player, "satell",
                                  bulletsindeg),
                            Enemy(scr, random.randint(0, 780), -random.randint(10, 200), player, "satell",
                                  bulletsindeg),
                            Enemy(scr, random.randint(0, 780), -random.randint(10, 200), player, "satell",
                                  bulletsindeg),
                            Enemy(scr, random.randint(0, 780), -random.randint(10, 200), player, "satell",
                                  bulletsindeg),
                            Enemy(scr, random.randint(0, 780), -random.randint(10, 200), player, "satell",
                                  bulletsindeg),
                            Enemy(scr, random.randint(0, 780), -random.randint(10, 200), player, "satell",
                                  bulletsindeg)]
                    }),
        LevelCreate(4,
                    {
                        1: [Enemy(scr, random.randint(0, 780), -random.randint(10, 200), player, "fighter",
                                  bulletsindeg)
                            for f in range(6)] + [
                               Enemy(scr, random.randint(0, 780), -random.randint(10, 200), player, "satell",
                                     bulletsindeg) for f in range(4)]

                    })
    ]
    return levels


def click_button(ms):
    global run_levels, levels_data, screen, shipsP, bullets
    run_levels = False
    levels_data = create_levels(screen, shipsP, bullets)
    tms = int(ms)
    run(levels_data[tms - 1], tms)


def create_buttons(scr, levels):
    dx = 50
    dy = 100
    sdy = 100
    buttons = []
    line = 0
    for x in range(len(levels)):

        if line < 5:
            new_btn = Button(scr, (35, 34, 27), 50, 50, dx, dy, click_button, str(x + 1), None, (229, 228, 222),
                             "level", True)
            buttons.append(new_btn)
            dx += 50 * 2
            line += 1
        else:
            line = 0
            dy += sdy
    return buttons


levels_data = create_levels(screen, shipsP, bullets)
levels_button = create_buttons(screen, levels_data)


def run(enemies_list, ns):
    global menu, game, run_levels, money, pause, testMoney
    menu = False
    run_levels = False
    game = True
    pygame.display.set_caption("Космический бой")
    bg = pygame.image.load("IMG/Bg.png").convert_alpha()

    wavenumber = 1
    enemies.add(enemies_list.enemies[wavenumber])

    while game:
        if not pause:
            money = int(openTxt("upgrade_sts")["money"])
            Controls.events(shipsP, bullets, enemies, unPause)

            UpdateSCR(bg, screen, shipsP, bullets, enemies, bullets_enemy, static, TestSetMoney, testMoney)
            if len(enemies) <= 0:
                wavenumber += 1
                try:
                    enemies.add(enemies_list.enemies[wavenumber])
                except:
                    game = False
                    Reload()
                    lvldata = openTxt("levels_sts")
                    if len(lvldata) != ns:
                        lvldata[str(ns + 1)] = True
                        writeTxt("levels_sts", lvldata)
                    finishMenu()

            pygame.time.Clock().tick(90)
        else:
            def quitMenu():
                global game, pause
                game = False
                pause = False
                Levels()
                Reload()
                menu_pause.disable()

            def resume():
                global pause
                pause = False
                menu_pause.disable()        

            menu_pause = pygame_menu.Menu('Menu', 400, 400,
                                          theme=pygame_menu.themes.THEME_BLUE)
            menu_pause.add.button('Resume', resume)
            menu_pause.add.button('Quit', quitMenu)
            menu_pause.mainloop(screen)


def finishMenu():
    menu_finish = pygame_menu.Menu('Menu', 400, 400, theme=pygame_menu.themes.THEME_GREEN)
    menu_finish.add.label("Money:" + str(testMoney) + "$")
    menu_finish.add.label("AllMoney:" + openTxt("upgrade_sts")["money"] + "$")
    menu_finish.add.button('Go Menu', startLevel)
    menu_finish.mainloop(screen)


def startLevel():
    global testMoney
    SetMoney(testMoney)
    testMoney = 0
    Levels()


def unPause():
    global pause
    pause = True


def run_menu():
    pygame.init()
    global game, menu, run_levels
    menu = True
    run_levels = False
    game = False
    pygame.display.set_caption("Космический бой")
    bg_color = (76, 128, 141)
    button_start = Button(screen, (100, 103, 84), 310, 90, 80, 370, Levels, "Play", None, (0, 0, 0), "default", True)
    button_setting = Button(screen, (100, 103, 84), 310, 90, 80, 510, goSetting, "Setting", None, (0, 0, 0), "default",
                            True)
    button_quit = Button(screen, (100, 103, 84), 310, 90, 80, 650, Quit, "Quit", None, (0, 0, 0), "default", True)
    logo_img = pygame.transform.scale(pygame.image.load("IMG/pixil-layer-0.png").convert_alpha(), (320, 270))

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        button_start.update()
        button_setting.update()
        button_quit.update()
        font = pygame.font.SysFont("comicsansms", 150)
        text_surface = font.render("WarSpace", True, (234, 209, 70))
        screen.blit(logo_img, (440, 400))
        screen.blit(text_surface, (40, 50))
        pygame.display.flip()


def goSetting():
    global menu
    menu = False
    setting(run_menu)


def Levels():
    global menu, run_levels, game, screen
    menu = False
    run_levels = True
    game = False
    pygame.display.set_caption("Космический бой")
    home_button = Button(screen, (67, 68, 69), 105, 45, 50, 25, run_menu, "Home", None, (182, 189, 191), "default",
                         True)
    shop_button = Button(screen, (67, 68, 69), 105, 45, 200, 25, run_shop, "Shop", None, (182, 189, 191), "default",
                         True)
    bg_color = (76, 128, 141)
    time.sleep(0.1)
    while run_levels:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        home_button.update()
        shop_button.update()
        levels_static = openTxt("levels_sts")
        for h in levels_button:
            h.enabled = levels_static[h.message]
            h.update()
        pygame.display.flip()
        pygame.time.Clock().tick(90)


def run_shop():
    global run_levels, money
    run_levels = False
    shop(Levels, shipsP)


def Reload():
    global pause
    shipsP.health = shipsP.maxhealth
    bullets.empty()
    bullets_enemy.empty()
    enemies.empty()
    shipsP.mtop = False
    shipsP.mbottom = False
    shipsP.mleft = False
    shipsP.mright = False
    pause = False


static = Static(screen, shipsP, Levels, Reload)


def SetMoney(cash):
    money_gl = openTxt("upgrade_sts")
    local_money = int(money_gl["money"])
    local_money += cash
    money_gl["money"] = str(local_money)
    writeTxt("upgrade_sts", money_gl)


def TestSetMoney(cash):
    global testMoney
    testMoney += cash


def Quit():
    sys.exit()
