#include <stdio.h>
// 使用转移序列

int main(void)
{
  float salary;

  printf("\aEnter your desired monthly salary:\n");
  printf(" $______\b\b\b\b\b\b");

  scanf("%f", &salary);
  printf("\n\t$%.2f a month is $%.2f a year.", salary, salary * 12.0);
  printf("\rGee!\n");

  return 0;
}
