//
// Created by yum on 2025/12/10.
//
#include <stdio.h>
#include <string.h>

void find_track(char search_for[]) {
    char tracks[][80] = {
        "I left my heart in Harvard Med School",
        "Newark, Newark - a wonderful town",
        "Dancing with a Dork",
        "From here to maternity",
        "The girl from Iwo Jima",
    };
    printf(tracks[2]);
    // printf(tracks[2][5]);

    int i;
    for (i = 0; i < 5; i++) {
        if (strstr(tracks[i], search_for)) {
            printf("Track %i: '%s'\n", i, tracks[i]);
        }
    }
}

int main() {
    char s0[] = "dysfunctional";
    char s1[] = "fun";
    if (strstr(s0, s1)) {
        puts("我在 dysfunctional 中找到了 fun！\n");
    }
    find_track("Sinatra");
    return 0;
}
