#include <stdio.h>

void jolly(void);
void deny(void);

int main(void)
{
  int c = 3;

  while (c > 0)
  {
    jolly();
    --c;
  }

  deny();

  return 0;
}

void jolly(void)
{
  printf("For he's a jolly good fellow!\n");
}

void deny(void)
{
  printf("Which nobody can deny!\n");
}
