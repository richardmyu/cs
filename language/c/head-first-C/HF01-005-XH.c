//
// Created by yum on 2025/12/05.
//
#include <stdio.h>

int main() {
    int x = 0;
    int y = 0;
    while (x < 5) {
        // case 1
        // y = x - y;

        // case 2
        // y = y + x;

        // case 3
        /*y = y + 2;
        if (y > 4) {
            y = y - 1;
        }*/

        // case 4
        /*x = x + 1;
        y = y + x;*/

        // case 5
        if (y < 5) {
            x = x + 1;
            if (y < 3) {
                x = x - 1;
            }
        }
        y = y + 2;

        printf("%i%i ", x, y);
        x = x + 1;
    }
    return 0;
}
