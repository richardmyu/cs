#include <stdio.h>

/* 对 fahr = 0, 20, ..., 300
打印摄氏温度与华氏温度对照表 */
main()
{
  float fahr, celsius;
  int lower, upper, step;

  lower = 0;   /* 温度表的下限*/
  upper = 100; /* 温度表的上限*/
  step = 2;    /* 步长*/

  celsius = lower;
  printf("摄氏温度与华氏温度对照表\n");

  while (celsius <= upper)
  {
    fahr = celsius * 9.0 / 5.0 + 32.0;
    printf("%3.0f %6.2f\n", celsius, fahr);
    celsius = celsius + step;
  }
}
