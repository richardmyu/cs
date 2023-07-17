#include <stdio.h>

/* 统计空格、制表符和换行符个数 */
int main()
{
  long c, nl;

  nl = 0;

  while ((c = getchar()) != EOF)
    /* TODO: 空格匹配有问题 */
    if (c == '\\' || c == '\n' || c == '\t')
      ++nl;
  printf("%d\n", nl);
}
