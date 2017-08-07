
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

# 初始化游戏性并创建一个屏幕对


def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    # 创建一个存储子弹的编组
    bullets = Group()
    ship = Ship(ai_setting, screen)
    # 开始游戏住循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_event(ship,ai_setting,screen, bullets)
        ship.update()
        bullets.update()
        # 每次循环都重新绘制屏幕
        gf.update_screen(ai_setting, screen, ship, bullets)

run_game()











