"""
2、信号量---multiprocess.Semaphore
    - 信号量的实现机制：计数器 + 锁 实现的

    互斥锁同时只允许一个线程更改数据，而信号量Semaphore是同时允许一定数量的线程更改数据 。
    假设商场里有4个迷你唱吧，所以同时可以进去4个人，如果来了第五个人就要在外面等待，等到有人出来才能再进去玩。
    实现：
    信号量同步基于内部计数器，每调用一次acquire()，计数器减1；每调用一次release()，计数器加1.当计数器为0时，acquire()调用被阻塞。这是迪科斯彻（Dijkstra）信号量概念P()和#V()的Python实现。信号量同步机制适用于访问像服务器这样的有限资源。
    信号量与进程池的概念很像，但是要区分开，信号量涉及到加锁的概念
"""

import time
import random
from multiprocessing import Process, Semaphore


def ktv(person, sem):
    sem.acquire()
    print('\033[32m%s走进ktv\033[0m' % person)
    time.sleep(random.randint(1,5))
    print('\033[31m%s走出ktv\033[0m' % person)
    sem.release()


if __name__ == '__main__':
    sem = Semaphore(4)  # 限定4个
    for i in range(10):
        p = Process(target=ktv, args=('person%s' % i, sem))
        p.start()
