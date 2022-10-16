#include <stdio.h>

int y = 1;
int main()
{
  int x = 4;
  // printf("X 保存在 %p\n", &x);
  printf("X 保存在 %li\n", &x);
  return 0;
}
