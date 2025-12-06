//
// Created by yum on 2025/12/04.
//
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    char card_name[3];
    puts("请输入牌名： ");
    scanf("%2s", card_name);
    int val = 0;

    if (card_name[0] == 'K') {
        val = 10;
    } else if (card_name[0] == 'Q') {
        val = 10;
    } else if (card_name[0] == 'J') {
        val = 10;
    } else if (card_name[0] == 'A') {
        val = 11;
    } else {
        val = atoi(card_name);
    }
    if (val > 2 && val < 7) {
        puts("计数增加");
    } else if (val == 10) {
        puts("计数减少");
    }
    return 0;
}
