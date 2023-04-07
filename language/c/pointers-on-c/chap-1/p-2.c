#include <stdio.h>

int main()
{
  char flag;

  while (flag != 'q')
  {
    printf("enter something: ");
    scanf("%s", &flag);
    printf("%s\n", flag);
  }

  return 0;
}
