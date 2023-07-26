#include <stdio.h>

#include <stdio.h>

/* 以每行一个单词的形式打印输入 */

/*
int main()
{

  int c;

  while ((c = getchar()) != EOF)
  {
    if (c == ' ' || c == '\n' || c == '\t')
      // printf("\n%d\n", c);
      putchar(c);
  }
}
*/

#define IN 1  /*  在单词内 */
#define OUT 0 /*  在单词外 */

int main()
{
  /*
    nl 行数
    nw 单词数
    nc 字符数
  */
  int c, state;
  state = OUT;

  while ((c = getchar()) != EOF)
  {
    if (c == ' ' || c == '\n' || c == '\t')
    {
      putchar('\n');
      state = OUT;
    }
    else if (state == OUT)
    {
      state = IN;
      putchar(c);
    }
    else
    {
      putchar(c);
    }
  }
}
