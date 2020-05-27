# -*- coding: utf-8 -*-

def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        # print("\nSorry, the file " + filename + " does not exist.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("\nThe file " + filename + " has about " + str(num_words) + " words.")


filenames = ['alice.txt', 'pi_digits.txt', 'xhr.txt', 'programming.txt']
for filename in filenames:
    count_words(filename)
