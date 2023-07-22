#include <stdio.h>

/* 将输入复制到输出，且将
  制表符 --> \t
  回退符 --> \b
  反斜杠 --> \\

case1 正则匹配
case2 遍历替换
TODO: 语法未知
*/
int main()
{
  long c;

  while ((c = getchar()) != EOF)
  {
    if (c == '\t')
      printf("\\t");
    if (c == '\b')
      printf("\\b");
    if (c != '\b')
      if (c != '\t')
        if (c != '\\')
          putchar(c);
  }
}
