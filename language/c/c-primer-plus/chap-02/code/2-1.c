#include <stdio.h>
/*
#include <stdio.h>
一条 C 预处理器指令（preprocessor directive）
通常 C 编译器在编译前会对源代码做一些准备工作，即 预处理（preprocessing）

stdio.h
含义：标准输入/输出头文件

头文件
通常在 C 程序顶部发信息集合被称为 头文件（header）

*/

/*
int
表明 main 函数返回一个整数
返回给操作系统

main
函数名，C 程序一定从 main 函数开始执行（暂不考虑例外情况）

void
表明 main 函数不带任何参数
*/
int main(void) /* 一个简单的 C 程序 */
{
  /*
  {}
  标记函数体的开始和结束

  还可用于把函数中的多条语句合并为一个单元或块
  */

  int num;
  /*
  int num
  声名（declaration），定义变量 num
  所有变量必须先声名才能使用

  int
  关键字（keyword），表示一种基本的 C 语言数据类型

  num
  标识符（identifier），变量、函数或其他实体的名称
  */

  num = 1; /* 为 num 赋值 */

  printf("I am a simple "); // 这也是注释，单行注释 C99 新增
  printf("computer.\n");
  printf("My favorite number is %d because it is first.\n", num);

  return 0;
}
