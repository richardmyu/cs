# -*- coding: utf-8 -*-
'''
@Time: 2022/10/01 22:58:43
@Author: yum
@Email: richardminyu@foxmail.com
@File: alien_invasion.py


'''

import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group


def run_game():
    # 初始化 pygame，设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建飞船
    ship = Ship(ai_settings, screen)

    # 创建子弹编组
    bullets = Group()

    # 开始游戏主循环
    while True:
        gf.chunk_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
