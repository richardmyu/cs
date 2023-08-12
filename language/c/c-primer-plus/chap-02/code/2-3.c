/*
一个文件包含两个函数
*/

#include <stdio.h>

void butler(void);
/*
ANSI/ISO c 函数原型（prototype）

函数原型是一种声明形式，告知编译器在程序中要使用该函数
因此函数原型也被称为 函数声明（function declaration）
函数原型指明了函数的属性

C 标准建议，要为程序中用到的所有函数提供函数原型
*/

int main(void)
{
  printf("I will summon the butler function.\n");
  butler(); /* 函数调用（function call） */
  printf("Yes. Bring me some tea and writeable DVDs.\n");

  return 0;
}

/*
函数定义（function definition）
函数定义的位置不影响执行的时机
何时执行取决与何处何时调用
*/
void butler(void)
{
  printf("You rang, sir?\n");
}
