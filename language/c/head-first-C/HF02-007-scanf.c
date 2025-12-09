#include <stdio.h>
//
// Created by yum on 2025/12/09.
//
int main() {
    char name[40];
    int age;
    printf("Enter your name: ");
    scanf("%3s", name); // scanf 会导致缓冲区溢出
    // fgetc(name,40,stdin);
    //siezeof 接受字符串最大长度（含 `\0`）；stdin 表示数据来自键盘

    printf("Hello, %s!\n", name);

    printf("Enter your age: ");
    scanf("%i", &age);
    printf("oh, you are %i years old.", age);

    return 0;
}
