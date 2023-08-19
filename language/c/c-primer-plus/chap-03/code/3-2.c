#include <stdio.h>

int main(void)
{
  int ten = 10;
  int two = 2;

  printf("Doing it right: ");
  printf("%d minus %d is %d\n", ten, 2, ten - two);
  printf("Doing it wrong: ");

  // 后两个 %d 没有提供任何值
  // 所有打印出的值是内存中的任意值
  printf("%d minus %d is %d\n", ten);

  return 0;
}
