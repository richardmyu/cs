#include <stdio.h>

/* 常量
注意：#define 后面没有分号
 */
#define LOWER 0   /* 温度表的下限*/
#define UPPER 300 /* 温度表的上限*/
#define STEP 20   /* 步长*/

/* 对 fahr = 0, 20, ..., 300
打印华氏温度与摄氏温度对照表 */
int main()
{
  int fahr;

  for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)
  {
    printf("%3d %6.1f\n", fahr, (5.0 / 9.0) * (fahr - 32));
  }
}
