from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载: %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s 下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    download_task('健康指北.pdf')
    download_task('天空之城.mp4')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
