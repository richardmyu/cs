#include <stdio.h>
#include <stdlib.h>

void hanoi(int n, char x, char y, char z);

void hanoi(int n, char x, char y, char z)
{
  if (n == 0)
  {
    /* do nothing */
  }
  else
  {
    hanoi(n - 1, x, z, y);
    printf("%c->%c, ", x, y);
    hanoi(n - 1, z, y, x);
  }
}

int main(void)
{
  // hanoi(6, 'A', 'B', 'C');
  hanoi(3, 'A', 'B', 'C');
  return EXIT_SUCCESS;
}
