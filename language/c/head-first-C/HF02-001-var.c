//
// Created by yum on 2025/12/06.
//
#include <stdio.h>

int y = 1;

int main() {
    int x = 4;
    printf("x=%i 保存在：%p\n", x, &x);
    printf("y=%i 保存在：%p\n", y, &y);

    return 0;
}
