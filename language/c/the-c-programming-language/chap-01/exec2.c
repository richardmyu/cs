#include <stdio.h>

int main()
{
  printf("hello \c world");
  // warning: unknown escape sequence : '\c' printf("hello world!\c\b");
}

// hello c worldhello world !c
