#include <stdio.h>

int main()
{
  // p1
  int card_count = 11;

  if (card_count > 10)
    puts("这副牌赢面很大，我要加注！");

  // p2
  int c = 10;
  while (c > 10)
  {
    puts("我决不在课堂上写代码！");
    c = c - 1;
  }

  // p3
  char f[20];
  puts("输入朋友的名字：");
  scanf("%19s", f);
  printf("Hello, %s, how are you?\n", f);

  // p4
  char suit = 'H';
  switch (suit)
  {
  case 'C':
    puts("梅花 clubs");
    break;
  case 'D':
    puts("方块 diamonds");
    break;
  case 'H':
    puts("红心 hearts");
    break;
  default:
    puts("黑桃 spades");
  }

  return 0;
}
