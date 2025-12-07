#include <stdio.h>
//
// Created by yum on 2025/12/07.
//
int main(int argc, char *argv[]) {
    char s[] = "How big is it?";
    char *t = s;
    printf("%s(%p)=%i\n", s, &s, sizeof(s));
    printf("%s(%p)=%i\n", t, &t, sizeof(t));
    // printf("%s()=\n", s[0]);
}
