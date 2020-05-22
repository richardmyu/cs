# include <stdio.h>
# 05/04/20 21:41

int main()
{
    printf("请输入身高的英寸和英寸：");
    int foot;
    int inch;
    scanf("%d %d", &foot, &inch);
    printf("身高是%f米。\n", ((foot + inch / 12.0) * 0.3048));
    return 0;
}
