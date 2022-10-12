# -*- coding: utf-8 -*-

import sys
import pygame


class Settings():

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.img_speed_factor = 1


class Img():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # 小数
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 移动
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.img_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.img_speed_factor
        elif self.moving_top and self.rect.top > 0:
            self.centery -= self.ai_settings.img_speed_factor
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.img_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery


def check_events(img):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 按下键盘
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                img.moving_right = True
            elif event.key == pygame.K_LEFT:
                img.moving_left = True
            elif event.key == pygame.K_UP:
                img.moving_top = True
            elif event.key == pygame.K_DOWN:
                img.moving_bottom = True
        # 释放键盘
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                img.moving_right = False
            elif event.key == pygame.K_LEFT:
                img.moving_left = False
            elif event.key == pygame.K_UP:
                img.moving_top = False
            elif event.key == pygame.K_DOWN:
                img.moving_bottom = False


def update_screen(ai_settings, screen, img):
    screen.fill(ai_settings.bg_color)
    img.blitme()
    pygame.display.flip()


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('start')

    img = Img(ai_settings, screen)

    while True:
        check_events(img)
        img.update()
        update_screen(ai_settings, screen, img)


run_game()
