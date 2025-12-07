#include <stdio.h>
//
// Created by yum on 2025/12/07.
//
void skip(char *msg) {
    puts(msg + 6);
    // puts(msg[6]);
}

int main(int argc, char *argv[]) {
    int drinks[] = {4, 2, 3};
    printf("第一单： %i 杯\n", drinks[0]);
    printf("第二单： %i 杯\n", *drinks);

    printf("第三单： %i 杯\n", drinks[2]);
    printf("第三单： %i 杯\n", *(drinks + 2));

    char *msg_from_amy = "Don't call me";
    skip(msg_from_amy);

    int nums[] = {1, 2, 3};
    printf("nums 的地址是 %p\n", nums);
    printf("nums + 1 的地址是 %p\n", nums + 1);
}
