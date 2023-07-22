#include <stdio.h>

/* 统计空格、制表符和换行符个数 */
int main()
{
  /*
  long c, nl;

  nl = 0;

  while ((c = getchar()) != EOF)
    // TODO: 空格匹配有问题
    if (c == '\\' || c == '\n' || c == '\t')
      ++nl;
  printf("%d\n", nl);
  */
  int c, nb, nt, nl;

  nb = 0; // 空格
  nt = 0; // 制表符
  nl = 0; // 换行符

  while ((c = getchar()) != EOF)
  {
    if (c == ' ')
      ++nb;
    if (c == '\t')
      ++nt;
    if (c == '\n')
      ++nl;
  }

  printf("%d %d %d\n", nb, nt, nl);
}
