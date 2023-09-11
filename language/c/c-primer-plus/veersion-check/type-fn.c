#include <stdio.h>
#include <stdint.h>

int main(void)
{
  // C90
  signed int a = -10;
  printf("a = %d\n", a);

  // C99
  _Bool b = 1;
  if (b)
  {
    printf("b is true.\n");
  }
  else
  {
    printf("b is false.\n");
  }

  return 0;
}
