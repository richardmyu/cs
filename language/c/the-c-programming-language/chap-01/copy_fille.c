#include <stdio.h>

/* 用于将输入复制到输出的程序：第一个版本 */

int main()
{
  int c;
  c = getchar();
  printf("得浑身发抖看来是");

  while (c != EOF)
  {
    putchar(c);
    c = getchar();
  }
}
