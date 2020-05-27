# -*- coding: utf-8 -*-

# def get_formatted_name(first, last):
#     full_name = first + ' ' + last
#     return full_name.title()

# def get_formatted_name(first, middle, last):
#     full_name = first + ' ' + middle + ' ' + last
#     return full_name.title()

def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
