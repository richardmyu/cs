//
// Created by yum on 2025/12/06.
//
#include <stdio.h>
#include <stdlib.h>

int main() {
    char card_name[3];
    int count = 0;
    do {
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
            case 'X':
                puts("over");
                // break; // 终止 switch，但没有跳出 do while，循环体后面的代码还会执行
                continue; // 跳出本轮 do while，进行下一轮 do while ；执行条件不符合，跳出循环
            default:
                val = atoi(card_name);

                if (val < 1 || val > 10) {
                    puts("error!");
                    continue;
                }
        }

        if (val > 2 && val < 7) {
            puts("计数增加");
            count++;
        } else if (val == 10) {
            puts("计数减少");
            count--;
        }

        printf("当前计数：%i\n", count);
    } while (card_name[0] != 'X');
    return 0;
}
