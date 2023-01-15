# -*- coding: utf-8 -*-


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计以后，都将其移到列表 completed_models 中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print('Printing model: ' + current_design)

        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示所有打印好的模型"""
    print('\nThe following models have been printed.')

    for item in completed_models:
        print(item)
