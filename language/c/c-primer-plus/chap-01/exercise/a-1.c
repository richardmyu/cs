#include <stdio.h>

int main()
{
  int l = 0;

  printf("Please enter a number: ");

  while ((l = getchar()) != EOF)
  {
    // printf("%d\n", l);
    putchar(l);
    printf("%.2d\n", l * 2.54);
  }
}
