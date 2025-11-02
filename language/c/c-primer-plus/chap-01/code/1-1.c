#include <stdio.h>

int main(void)
{
  int dogs;
  printf("Hello world!\n");
  printf("How many dogs do you have?\n");
  scanf("%d", &dogs);
  system("pause");
  printf("So you have %d dog(s)!\n", dogs);

  return 0;
}

