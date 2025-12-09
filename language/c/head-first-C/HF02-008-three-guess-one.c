//
// Created by yum on 2025/12/09.
//
#include <stdio.h>

int main() {
    // char *cards = "JQK";
    char cards[] = "JQK";
    const char *s = "something was wrong";
    // s[0] = 'S';

    char a_card = cards[2];
    cards[2] = cards[1];
    cards[1] = cards[0];
    cards[0] = cards[2];
    cards[2] = cards[1];
    cards[1] = a_card;
    puts(cards);
    return 0;
}
