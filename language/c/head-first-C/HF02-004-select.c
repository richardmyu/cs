//
// Created by yum on 2025/12/07.
//
#include <stdio.h>

int main(int argc, char *argv[]) {
    int contestants[] = {1, 2, 3};
    int *choice = contestants; // *choice == contestants[0]
    printf("000 contestants[0]=%i,contestants[1]=%i,contestants[2]=%i \n", contestants[0], contestants[1], contestants[2]);
    printf("choice %d\n", *choice);

    contestants[0] = 2;
    printf("111 contestants[0]=%i,contestants[1]=%i,contestants[2]=%i \n", contestants[0], contestants[1], contestants[2]);
    printf("choice %d\n", *choice);

    contestants[1] = contestants[2];
    printf("222 contestants[0]=%i,contestants[1]=%i,contestants[2]=%i \n", contestants[0], contestants[1], contestants[2]);
    printf("choice %d\n", *choice);

    contestants[2] = *choice;
    printf("333 contestants[0]=%i,contestants[1]=%i,contestants[2]=%i \n", contestants[0], contestants[1], contestants[2]);
    printf("choice %d\n", *choice);

    printf("我选 %i 号男嘉宾\n", contestants[2]);
    return 0;
}
