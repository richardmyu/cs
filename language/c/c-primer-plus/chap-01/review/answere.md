# Answer

1.对编程而言，可移植性意味着什么？

在一种系统中编写的C程序稍作修改或不修改就能在其他系统运行。如需修改，也只需要更改主程序头文件中的少许项即可。

2.解释源代码文件、目标代码文件和可执行文件有什么区别？

源代码文件：用来储存使用C语言编写的程序内容。

目标代码文件：或简称目标文件，用来储存源代码转换后的机器语言代码。

可执行文件：用计算机的机器语言表示代码的文件。编译器把源代码转换成中间代码，链接器把中间代码和其他代码合并，生产可执行的代码文件。

3.编程的7个主要步骤式什么？

1）定义程序的目标

想要程序去做什么首先自己要明确自己要做什么，思考你的程序需要哪些信息，要进行那些计算和控制，以及程序应该要报告什么信息。

2）设计程序

对程序应该完成什么任务有概念性的认识后，就应该考虑如何用程序来完成它。

除此之外，还要决定在程序（可能时复制文件）中如何表示数据，以及用什么方法处理数据。

3）编写代码

设计好程序后，就可以编写代码来实现它。也就是说，把你设计的程序翻译成 C 语言。

在这一步骤中，应该给自己编写的程序添加文字注释。

4）编译

【编译的细节取决于编程的环境。】

接下来的这一步是编译源代码。编译器把源代码转换成可执行代码的程序。

编译器还会检查C 语言程序是否有效。如果C编译器发现错误，就不生成可执行文件并报错。理解特定编译器报告的错误或警告信息是程序员要掌握的另一项技能。

5）运行程序

传统上，可执行文件是可运行的程序。

6）测试和调试程序

接下来，应该检查程序是否安装你设计的思路运行。查找并修复程序错误的过程叫**调试**。

7）维护和修改程序

创建完程序后，你发现程序有错，或指箱扩展程序的用途，这是就要修改程序。如果在编写程序时清除地做了注释并采用了合理的设计方案，这些事情都很简单。

【编程并非像描述那样是一个线性的过程。有时，要在不同的步骤之间往复。】
【磨刀不误砍柴工，应该养成先规划再动手编写代码的好习惯，用纸和笔记录下程序的目标和设计框架。这样在编写代码的过程中会更加得心应手、条理清晰。】

4.编译器的主要任务是什么？

将源代码转换成可执行的（机器语言）代码。

5.链接器的主要任务是什么？

合并源代码的中间代码和 C 库，形成最终的程序代码。
