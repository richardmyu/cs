#include <stdio.h>

int main()
{
  long c, nl;

  nl = 0;
  while ((c = getchar()) != EOF)
    /* \n == 10 */
    if (c == '\n')
      ++nl;

  printf("%d\n", nl);
}
