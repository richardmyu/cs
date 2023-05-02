"""排序算法
选择
冒泡
归并
"""


def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]

    for i in range(len(items) - 1):
        min_index = i

        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j

        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(items, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = items[:]

    for i in range(len(items) - 1):
        swapped = False

        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True

        if not swapped:
            break

    return items


def advance_bubble_sort(items, comp=lambda x, y: x > y):
    """搅拌排序(冒泡排序升级版)"""
    items = items[:]

    for i in range(len(items) - 1):
        swapped = False

        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True

        if swapped:
            swapped = False

            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True

        if not swapped:
            break

    return items


def merge(items1, items2, comp=lambda x, y: x < y):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0

    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1

    items += items1[index1:]
    items += items2[index2:]
    return items


def merge_sort(items, comp=lambda x, y: x < y):
    return _merge_sort(list(items), comp)


def _merge_sort(items, comp):
    """归并排序"""

    if len(items) < 2:
        return items

    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def main():
    list = [1, 2, 4, 12, 3, 17, 9, 111, 5, 32, 6, 234]
    print("list: ", list)
    print("list(select_sort): ", select_sort(list))
    print("list(bubble_sort): ", bubble_sort(list))
    print("list(advance_bubble_sort): ", advance_bubble_sort(list))
    list2 = [7, 11, 8, 120, 24, 46]
    print("list(merge): ", merge(list, list2))
    print("list(merge_sort): ", merge_sort(list))


if __name__ == '__main__':
    main()
