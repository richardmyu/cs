#include <stdio.h>

#define BR_TEXT "Brazil, Russia"
#define IC_TEXT "India, China"

void br(void);
void ic(void);

int main(void)
{
  br();
  printf(",");
  ic();
  printf("\n");
  ic();
  printf(",\n");
  br();

  return 0;
}

void br(void)
{
  printf("%s", BR_TEXT);
}

void ic(void)
{
  printf("%s", IC_TEXT);
}
