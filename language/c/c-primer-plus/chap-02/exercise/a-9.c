#include <stdio.h>

int main(void)
{
  int x, y;

  x = 10;
  y = 5;     /* 7 */
  y = x + y; /* 8 */
  x = x * y; /* 9 */

  printf("%d %d\n", x, y);

  return 0;
}

// x = 10 * 15 = 150
// y = 5 + 10 = 15
