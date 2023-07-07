#include <stdio.h>

/* 对 fahr = 0, 20, ..., 300
打印华氏温度与摄氏温度对照表 */
int main()
{
  int fahr, celsius;
  int lower, upper, step;

  lower = 0;   /* 温度表的下限*/
  upper = 300; /* 温度表的上限*/
  step = 20;   /* 步长*/

  fahr = lower;
  while (fahr <= upper)
  {
    celsius = 5 * (fahr - 32) / 9;
    /* celsius = (fahr - 32) * 5 / 9; 这样写可以*/
    /* celsius = (fahr - 32) * (5 / 9);
    这样写不可以，因为 5/9 的结果被截取，
    小数点后面都丢弃，得到 0
    */

    /*
    printf 函数并不是 C 语言本身的一部分
    C 语言本身没有定义输入输出功能
    printf 是标准库函数中一个函数
    标准库函数一般在 C 程序中都可以使用
    */
    printf("%d\t%d\n", fahr, celsius);
    // printf("%3d %6d\n", fahr, celsius);
    fahr = fahr + step;
  }
}
