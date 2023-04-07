#include <stdio.h>

void fn1()
{
  int x = 0;
  int y = 0;

  while (x < 5)
  {
    y = x - y;
    printf("%i%i ", x, y);
    x += 1;
  }
}

void fn2()
{
  int x = 0;
  int y = 0;

  while (x < 5)
  {
    y = x + y;
    printf("%i%i ", x, y);
    x += 1;
  }
}

void fn3()
{
  int x = 0;
  int y = 0;

  while (x < 5)
  {
    y = y + 2;
    if (y > 4)
    {
      y -= 1;
    }
    printf("%i%i ", x, y);
    x += 1;
  }
}

void fn4()
{
  int x = 0;
  int y = 0;

  while (x < 5)
  {
    x = x + 1;
    y = y + x;
    printf("%i%i ", x, y);
    x += 1;
  }
}

void fn5()
{
  int x = 0;
  int y = 0;

  while (x < 5)
  {
    if (y < 5)
    {
      x = x + 1;
      if (y < 3)
      {
        x -= 1;
      }
    }

    y += 2;
    printf("%i%i ", x, y);
    x += 1;
  }
}

int main()
{
  fn1();
  printf("\n");
  fn2();
  printf("\n");
  fn3();
  printf("\n");
  fn4();
  printf("\n");
  fn5();

  return 0;
}
