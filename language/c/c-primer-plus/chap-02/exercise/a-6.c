#include <stdio.h>

int main(void)
{
  // 关键字
  int main;

  // 关键字
  int int;
  // error:
  //   two or more data types in declaration specifiers

  // 关键字
  int function;

  // 关键字
  int char;
  // error:
  //   two or more data types in declaration specifiers

  // 关键字
  int = ;
  // error:
  //   expected identifier or '(' before '=' token

  return 0;
}
