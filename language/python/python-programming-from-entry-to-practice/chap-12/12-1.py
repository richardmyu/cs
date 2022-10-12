# -*- coding: utf-8 -*-

import pygame
import sys


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((300, 200))
    pygame.display.set_caption('start')
    bg_color = (30, 144, 255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()


run_game()
