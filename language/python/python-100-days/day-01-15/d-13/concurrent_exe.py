from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载: %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()

    # target : (传入一个函数)表示进程启动后要执行的代码
    # args : 是一个元组，它代表了传递给函数的参数
    p1 = Process(target=download_task, args=('健康指北.pdf',))

    # start方法用来启动进程
    p1.start()

    p2 = Process(target=download_task, args=('天空之城.mp4',))
    p2.start()

    # join 方法表示等待进程执行结束
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
