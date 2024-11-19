import pygame


def UpdateSCR(bg, screen, shipsP, bullets, enemies, bullets_enemy, static, setMoney, money):
    screen.blit(bg, (0, 0))
    for bullet in bullets.sprites():
        bullet.update()

        if bullet.rect.y < -2:
            bullet.kill()
            bullets.remove(bullet)
    for bullet in bullets_enemy.sprites():
        bullet.update()

        if bullet.rect.y > 810:
            bullet.kill()
            bullets.remove(bullet)
    enemies.update(enemies, setMoney)
    shipsP.update()
    shipsP.gun.update()
    static.update()
    font = pygame.font.SysFont("arial", 25)
    text_money = font.render("Money:" + str(money) + "$", True, (41, 206, 178))
    screen.blit(text_money, (20, 10))
    pygame.display.flip()

    pygame.time.Clock().tick(60)
