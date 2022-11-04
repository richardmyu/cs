# -*- coding: utf-8 -*-


def search(nums, target):
    for item in nums:
        if item == target:
            return nums.index(item)
    return -1


nums = [-1, 0, 3, 5, 9, 13]

print(search(nums, 2))
print(search(nums, 3))
print(search(nums, 9))
print(search(nums, -1))
