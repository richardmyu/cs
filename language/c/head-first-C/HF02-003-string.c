//
// Created by yum on 2025/12/07.
//
#include <stdio.h>

void fortune_cookie(char msg[]) {
    printf("Message reads: %s\n", msg);
    printf("msg occupies %i bytes\n", sizeof(msg));
}

int main() {
    char quote[] = "Cookies make you fat";
    printf("the quote is: %p\n", quote);
    fortune_cookie(quote);
}
