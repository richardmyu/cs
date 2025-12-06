//
// Created by yum on 2025/12/04.
//
#include <stdio.h>
#include <stdlib.h>

int main() {
    char card_name[3];
    puts("请输入牌名： ");
    scanf("%2s", card_name);
    int val = 0;

    switch (card_name[0]) {
        case 'K':
        case 'Q':
        case 'J':
            val = 10;
            break;
        case 'A':
            val = 11;
            break;
        default:
            val = atoi(card_name);
    }

    if (val > 2 && val < 7) {
        puts("计数增加");
    } else if (val == 10) {
        puts("计数减少");
    }

    return 0;
}
