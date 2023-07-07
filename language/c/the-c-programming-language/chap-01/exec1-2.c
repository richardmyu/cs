#include <stdio.h>

int main()
{
  // exec 1
  // printf("hello
  // world");
  // error: missing terminating " character

  // exec 2
  printf("hello \c world");
  // warning: unknown escape sequence : '\c'
}
