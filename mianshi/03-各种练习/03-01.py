"""
说出下列程序的打印结果
"""
import time
from multiprocessing import Process


def func1():
    count = 1
    while 1:
        print(count * '*')
        time.sleep(0.5)
        count += 1


def func2():
    print('func2 start')
    time.sleep(5)
    print('func2 end')


if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.daemon = True
    p1.start()  # p1是守护进程
    p2 = Process(target=func2)
    p2.start()
    time.sleep(3)
    print('主进程')

















# 主进程会等待子进程完全结束才结束
# 守护进程会随着主进程的代码执行完毕而结束
# 如果主进程代码已经执行完毕，但是子进程还没执行完，守护进程都不会继续执行
# 守护进程会随着主进程的代码执行完毕而结束
# 主进程会等待子进程结束，守护进程只等待主进程代码结束就结束了
