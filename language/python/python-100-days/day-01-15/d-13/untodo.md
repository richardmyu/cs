# untodo

1. 使用 subprocess 模块中的类和函数来创建和启动子进程，然后通过管道来和子进程通信

2. 使用 multiprocessing 模块中的 Queue 类，它是可以被多个进程共享的队列，底层是通过管道和信号量（semaphore）机制来实现的（解决 [ping-pong.py](./ping_pong.py))
