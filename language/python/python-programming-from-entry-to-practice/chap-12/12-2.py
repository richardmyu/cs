# -*- coding: utf-8 -*-

import sys
import pygame


class Settings:
    def __init__(self):
        self.screen_width = 300
        self.screen_height = 200
        self.bg_color = (230, 230, 230)


class Img:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height)
    )
    pygame.display.set_caption('start')
    img = Img(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_setting.bg_color)
        img.blitme()
        pygame.display.flip()


run_game()
