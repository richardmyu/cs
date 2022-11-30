# questions

## Q1

例子使用规则空白，是为了方便阅读代码。

## Q2

1.提高阅读性；
2.按需引用，减少内存浪费；
3.避免重复引入；

## Q3

1.阅读性高；
2.方便统一修改；

## Q4

```c
printf("%d\n", 1);
printf("%s\n", "12");
printf("%g\n", 1.2);
```

## Q5

```c
int quantity;
int price;
int department[2];

scanf("%d", &quantity);
scanf("%d", &price);
scanf("%d", &department[1]);
```

## Q6

提高运行速度

## Q7

- `char *strcpy(char *dest, const char *src)` 把 `src` 所指向的字符串复制到 `dest`。
- `char *strncpy(char *dest, const char *src, size_t n)` 把 `src` 所指向的字符串复制到 `dest`，最多复制 `n` 个字符。当 `src` 的长度小于 `n` 时，`dest` 的剩余部分将用空字节填充。

1.溢出；

## Q8
