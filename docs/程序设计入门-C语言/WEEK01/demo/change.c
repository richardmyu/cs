# include <stdio.h>

int main() {
	int amount = 100;
	printf("请输入总额（元）");
	scanf("%d", &amount);
	
	int price= 0;
	printf("请输入金额（元）");
	scanf("%d", &price);

	int change = amount - price;
	printf("找你%d元\n", change);

	int i;
	printf("%d\n", i);

	int j;
	printf("%d\n", j);
	return 0;
}
