# -*- coding: utf-8 -*-
'''
@Time: 2022/10/01 23:05:09
@Author: yum
@Email: richardminyu@foxmail.com
@File: settings.py


'''


class Settings():
    '''存储游戏所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
