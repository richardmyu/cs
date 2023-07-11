#include <stdio.h>

int main()
{
  int c;

  /* 在 C 语言中，诸如 c = getchar() 之类的赋值操作是一个表达式，
  因而就有一个值，即赋值后位于 = 左边变量的值。
  */
  while ((c = getchar()) != EOF)
  {
    putchar(c);
  }
}
