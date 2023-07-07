#include <stdio.h>

/* 对 fahr = 0, 20, ..., 300
打印华氏温度与摄氏温度对照表 */
int main()
{
  float fahr, celsius;
  int lower, upper, step;

  lower = 0;   /* 温度表的下限*/
  upper = 300; /* 温度表的上限*/
  step = 2;    /* 步长*/

  fahr = lower;
  printf("华氏温度与摄氏温度对照表\n");

  while (fahr <= upper)
  {
    celsius = 5.0 * (fahr - 32.0) / 9.0;
    printf("%3.0f %6.2f\n", fahr, celsius);
    fahr = fahr + step;
  }
}
