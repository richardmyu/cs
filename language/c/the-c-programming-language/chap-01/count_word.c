#include <stdio.h>

#define IN 1  /*  在单词内 */
#define OUT 0 /*  在单词外 */

/* 统计输入的行数、单词数与字符数 */
/* TODO: bug

case 01
---------------
hello


world

3 2 13
---------------

case 02
---------------
hello


world
2 1 7
---------------

最后一行的单词句子，如果没有确定(Enter)，则不参与计数

*/
int main()
{
  /*
    nl 行数
    nw 单词数
    nc 字符数
  */
  int c, nl, nw, nc, state;
  state = OUT;
  nl = nw = nc = 0;

  while ((c = getchar()) != EOF)
  {
    ++nc;

    if (c == '\n')
      ++nl;

    if (c == ' ' || c == '\n' || c == '\t')
      state = OUT;

    else if (state == OUT)
    {
      state = IN;
      ++nw;
    }
  }

  printf("\n%d %d %d\n", nl, nw, nc);
}
