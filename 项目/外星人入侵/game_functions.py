import sys
import pygame
from Bullet import Bullet

def check_event(ship,ai_setting,screen, bulletS):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            # 响应按键事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,ai_setting,screen, bulletS)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_setting, screen, ship,bullets):

    screen.fill(ai_setting.bg_color)
    # 在飞船和外星人后面绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        print("子弹的x坐标是" + str(bullet.rect.x))
        print("子弹的y坐标是" + str(bullet.rect.y))
        print(bullet.color)


    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def check_keydown_events(event, ship,ai_setting,screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一个子弹将其加入到编组中
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)




def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False