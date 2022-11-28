/*
** 这个程序从标准输入中读取输入行并在标准输出中打印这些输入行
** 每个输入行的后面一行是改行内容的一部分
**
** 输入的第 1 行是一串列标号，串的最后以一个负数结尾
** 这些列标号成对出现，说明需要打印的输入行的列的范围
** 例如， 0 3 10 12 -1 表示第 0 列到第 3 列，第 10 列到第 12 列的内容将被打印
** == 注释不能嵌套
*/

/*
** 在 c 中“注释”代码
** 注释代码而不删除，在其他语言中或许可行，但在 c 中不是好主意
** 从逻辑上删除 c 代码，更好的办法是使用 #if 指令
** 在 #if 和 #endif 之间的程序可以有效的从程序中去除
*/
#if 0
    statements
#endif

/*
** 预处理指令（preprocessor directives）
** 因为它们是由预处理器（preprocessor）解释的
** 预处理器读取源代码 --> 根据预处理指令对其修改 --> 将修改后的源代码递交编译器
** 1.#include
**  预处理器用名叫 stdio.h 的库函数头文件的内容替换 #include 指令语句
** 2.#define
**  将 MAX_COLS 定义为 20，这个名字出现在源文件任何地方，都会被替换为定义的值
**  一般都大写，和其他语言符号常量的作用类似
*/

#include <stdio.h> /*  */
#include <stdlib.h>
#include <string.h>
#define MAX_COLS 20    /* 所能处理的最大列号 */
#define MAX_INPUT 1000 /* 每个输入行的最大长度 */

/*
** 函数原型（function prototype）
** 告诉编译器这些以后将在源文件中定义的函数的特征
** 当函数被调用时，编译器就能对它们进行准确性检查
**   返回值类型 函数名 参数
**   int read_column_numbers(int columns[], int max);
**
** 指针（pointer）
** 在 rearrange 函数中，有四个参数，前两个参数都是指针
** 指针指定一个存储于计算机内存中的值的地址
** 第 2 和第 4 个参数被声明为 const，这表示函数将不会修改函数调用者所传递的这两个参数
** 关键字 void 表示函数不返回任何值
** 在其他语言中，不返回值的函数被称为 过程（procedure）
*/
int read_column_numbers(int columns[], int max);
void rearrange(char *output, char const *input, int n_columns, int const columns[]);

int main(void)
{
  int n_columns;          /* 进行处理的列标号 */
  int columns[MAX_COLS];  /* 需要处理的列数 */
  char input[MAX_INPUT];  /* 容纳输入行的数组 */
  char output[MAX_INPUT]; /* 容纳输出行的数组 */

  /*
  ** 读取该串列标号
  */
  n_columns = reda_column_numbers(columns, MAX_COLS);

  /*
   ** 读取、处理和打印剩余的输入行
   */
  while (gets(input) != NULL)
  {
    printf("Original input : %s\n", input);
    rearrange(output, input, n_columns, columns);
    printf("Rearranged line: %s\n", output);
  }

  return EXIT_SUCCESS;
}

/*
 ** 读取列标号，如果超出规定范围则不予理会
 */
int read_column_numbers(int columns[], int max)
{
  int num = 0;
  int ch;

  /*
   ** 取得列标号，如果所读取的数小于 0 则停止
   */
  while (num < max && scanf("%d", &columns[num]) == 1 && columns[num] >= 0)
  {
    num += 1;
  }

  /*
   ** 确认已经读取的标号为偶数个，因为它们是以对的形式出现的
   */
  if (num % 2 != 0)
  {
    puts("Last column number is not paired.");
    exit(EXIT_FAILURE);
  }

  /*
   ** 丢弃改行中包含最后一个数字的那部分内容
   */
  while ((ch = getchar()) != EOF && ch != '\n')
    ;

  return num;
}

/*
 ** 处理输入行，将指定列的字符连接在一起，输出行以 NUL 结尾
 */
void rearrange(char *output, char const *input, int n_columns, int const columns[])
{
  int col;        /* columns 数组的下标 */
  int output_col; /* 输出列计数器 */
  int len;        /* 输入行的长度 */

  len = strlen(input);
  output_col = 0;

  /*
   ** 处理每对列标号
   */
  for (col = 0; col < n_columns; col += 2)
  {
    int nchars = columns[col + 1] - columns[col] + 1;

    /*
     ** 如果输入行结束或输出行数组已满，就结束任务
     */
    if (columns[col] >= len || output_col == MAX_INPUT - 1)
      break;

    /*
     ** 如果输出行数据空间不够，只复制可以容纳的数据
     */
    if (output_col + nchars > MAX_INPUT - 1)
      nchars = MAX_INPUT - output_col - 1;

    /*
    ** 复制相关的数据
    */
    strncpy(output + output_col, input + columns[col], nchars);
    output_col += nchars;
  }

  output[output_col] = '\0';
}
