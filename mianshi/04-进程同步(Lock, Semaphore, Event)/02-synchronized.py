import time
from multiprocessing import Process, Lock


# 加了锁就把异步变成同步了
def func(num, lock):
    time.sleep(1)
    print('异步执行', num)  # 异步会同时开始

    lock.acquire()
    time.sleep(0.5)
    print('同步执行', num)  # 同步要一个结束才开始下一个
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=func, args=(i, lock))
        p.start()