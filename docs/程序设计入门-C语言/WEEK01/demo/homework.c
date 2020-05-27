# include <stdio.h>
 
int main()
{
    int initNum = 0;
    printf("请输入正三位数：");
    scanf("%d",&initNum);
    int a = initNum / 100;
    int b = (initNum % 100) /10;
    int c = (initNum % 100) % 10;
    int result = 0;
    if(a == 0){
        if(b == 0){
            if(c == 0){
                result = 0; 
            } else{
                result = c;
            }
        }else{
            result = c * 10 + b;
        }
    }else{
        if(b == 0){
            if(c == 0){
                result = a; 
            } else{
                result = c * 100 + a;
            }
        }else{
             if(c == 0){
                result = b * 10 + a; 
            } else{
                result = c * 100 + b * 10 + a;
            }
        }
    }
    printf("输出：%d", result);
    return 0;
}
