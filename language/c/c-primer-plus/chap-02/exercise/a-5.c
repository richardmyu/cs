#include <stdio.h>

void fn_1(void);
void fn_2(void);
void fn_3(void);
void fn_4(void);

int main(void)
{
  fn_1();
  fn_2();
  fn_3();
  fn_4();

  return 0;
}

void fn_1(void)
{
  printf("Baa Baa Black Sheep.");
}

void fn_2(void)
{
  printf("Have you any wool?\n");
}

void fn_3(void)
{
  printf("What!\nNo fish?\n");
}

void fn_4(void)
{
  int num;
  num = 2;
  printf("%d + %d = %d", num, num, num + num);
}
