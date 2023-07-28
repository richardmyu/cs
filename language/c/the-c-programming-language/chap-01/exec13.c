#include <stdio.h>

/*
编写一个程序，
打印其输入的文件中单词长度的直方图。
横条的直方图比较容易绘制，
竖条直方图则要困难些
*/

#define MAXHIST 15 /* 直方图最大长度 */
#define MAXWORD 11 /* 单词最大长度 */
#define IN 1       /* 在单词内 */
#define OUT 0      /* 在单词外 */

/* 打印水平直方图 */

int main()
{
  int c, i, nc, state;
  int len;         /* 每条长度 */
  int maxvalue;    /* wl[] 的最大值 */
  int ovflow;      /* 溢出单词的数量 */
  int wl[MAXWORD]; /* 单词个数 */

  state = OUT;
  nc = 0;     /* 单词中的字符数 */
  ovflow = 0; /* 超过最大单词长度的单词 */

  for (i = 0; i < MAXWORD; ++i)
  {
    wl[i] = 0;
  }

  while ((c = getchar()) != EOF)
  {
    if (c == '  ' || c == '\n' || c == '\t')
    {
      state = OUT;
      if (nc > 0)
      {
        if (nc < MAXWORD)
        {
          ++wl[nc];
        }
        else
        {
          ++ovflow;
        }
      }
      nc = 0;
    }
    else if (state == OUT)
    {
      state = IN;
      nc = 1; /* 开始下一个单词 */
    }
    else
    {
      ++nc; /* 插入单词 */
    }
  }

  maxvalue = 0;

  for (i = 1; i < MAXWORD; ++i)
  {
    wl[i] = 0;
  }
}
