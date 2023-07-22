#include <stdio.h>

#define NONBLANK 'a'

/* 将输入复制到输出，且将多个空格替换成一个空格
case1 正则匹配
case2 遍历替换
TODO: 语法未知
*/
int main()
{
  int c, lastc;

  lastc = NONBLANK;

  while ((c = getchar()) != EOF)
  {
    if (c != ' ')
      putchar(c);
    if (c == ' ')
      if (lastc != ' ')
        putchar(c);

    lastc = c;
  }
}
