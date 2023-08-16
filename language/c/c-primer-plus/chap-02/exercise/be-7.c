#include <stdio.h>

void sm(int n);

int main(void)
{
  int c = 3;

  while (c > 0)
  {
    sm(c);
    printf("\n");
    --c;
  }

  return 0;
}

void sm(int n)
{
  for (int i = 0; i < n; i++)
  {
    printf("Smile!");
  }
}
