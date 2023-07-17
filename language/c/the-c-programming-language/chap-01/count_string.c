#include <stdio.h>

/* 统计输入的字符-v1 */
int main()
{
  /*
  int  16位
  long 32位
  尽管在某些机器上 Int 与 long 类型的值具有同样的大小
  但在其他机器上 int 类型的值可能只有 16 位储存单元
  相当小的输入都可能使 int 类型的计数变量溢出
  */
  long nc;

  nc = 0;
  while (getchar() != EOF)

    /* nc = nc + 1; */
    ++nc;

  /* %ld -- long*/
  printf("%ld\n", nc);
}
