# Python 迭代器和生成器

```mermaid
graph LR
  A(a generator expression) & B(a generator function) --is--> C(a generator)
  C --always is--> D(an iterator) --next--> E(lazily produce next value)
  D --always is--> F
  F --iter--> D
  H(list/set/dict comprehension) --produces--> G(a container) --typically is--> F(iterable)
```

![py-iterator-generator-001](./py-iterator-generator-001.png)

## 容器 (container)

容器是一种把多个元素组织在一起的数据结构，容器中的元素可以逐个迭代获取，可以用 `in`，`not in` 关键字判断元素是否包含在容器中。通常这类数据结构把所有的元素存储在内存中（也有一些特例，并不是所有的元素都放在内存，比如迭代器和生成器对象），我们常用的 `string`、`set`、`list`、`tuple`、`dict` 都属于容器对象。

尽管大多数容器都提供了某种方式获取其中的每一个元素，但这并不是容器本身提供的能力，而是可迭代对象赋予了容器这种能力，当然并不是所有容器都是可迭代的。

## 可迭代对象

可以返回一个迭代器的对象都可以称之为可迭代对象。

```py
>>> x = [1, 2, 3]
>>> a = iter(x)
>>> b = iter(x)
>>> next(a)
1
>>> next(a)
2
>>> next(b)
1
>>> type(x)
<class 'list'>
>>> type(a)
<class 'list_iterator'>
>>> type(b)
<class 'list_iterator'>
```

可迭代对象和容器一样是一种通俗的叫法，并不是指某种具体的数据类型，`list` 是可迭代对象，`dict` 也是可迭代对象。`a` 和 `b` 是两个独立的迭代器，迭代器内部有一个状态，该状态用于记录当前迭代所在的位置，以方便下次迭代时获取正确的元素。迭代器有一种具体的迭代器类型，比如 `list_iterator`，`set_iterator`。可迭代对象实现了 `__iter__()` 方法，该方法返回一个迭代器对象。

当运行代码：

```py
x = [1, 2, 3]
for ele in x:
    ...
```

实际执行情况是：

![py-iterator-generator-002](./py-iterator-generator-002.png)

在循环遍历自定义容器对象时，会使用 python 内置函数 `iter()` 调用遍历对象的 `__iter__()` 获得一个迭代器，之后再循环对这个迭代器使用 `next()` 调用迭代器对象的 `__next__()`。`__iter__()` 只会被调用一次，而 `__next__()` 会被调用 n 次。

## Iterator（迭代器）

迭代器是一个带状态的对象，它能在你调用 `next()` 方法时返回容器中的下一个值，任何实现了 `__iter__()` 和 `__next__()` 方法的对象都是迭代器，`__iter__()` 返回迭代器自身，`__next__()` 返回容器中的下一个值，如果容器中没有更多元素了，则抛出 `StopIteration` 异常。

迭代器与列表的区别在于，构建迭代器的时候，不像列表把所有元素一次性加载到内存，而是以一种延迟计算（lazy evaluation）方式返回元素，这正是它的优点。比如列表中含有一千万个整数，需要占超过 100M 的内存，而迭代器只需要几十个字节的空间。因为它并没有把所有元素装载到内存中，而是等到调用 `next()` 方法的时候才返回该元素（按需调用 call by need 的方式，本质上 `for` 循环就是不断地调用迭代器的 `next()` 方法）。

itertools 模块里的函数返回的都是迭代器对象。为了更直观的感受迭代器内部的执行过程，我们自定义一个迭代器，以斐波那契数列为例：

> 见 [cust_iter.py](./cust_iter.py)

---

[Python 迭代器和生成器详解](https://zhuanlan.zhihu.com/p/341439647)
[Python 中的列表推导式和生成器表达式](https://zhuanlan.zhihu.com/p/124287514)
[Python 函数编程——列表生成式和生成器](https://www.cnblogs.com/Kwan-C/p/11529995.html)
