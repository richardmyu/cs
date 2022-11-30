#include <stdio.h>

int main()
{
  /* 1.7-4 */
  printf("%d\n", 1);
  printf("%s\n", "12");
  printf("%g\n", 1.2);

  /* 1.7-5 */
  int quantity;
  int price;
  int department[2];
  scanf("%d", &quantity);
  scanf("%d", &price);
  scanf("%d", &department[1]);
  printf("%d\n", quantity);
  printf("%d\n", price);
  printf("%d\n", department[1]);
  return 0;
}
