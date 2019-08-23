"""
3、事件---multiprocess.Event
    - 阻塞事件：wait()方法

    wait 是否阻塞是看 event 对象内部的一个属性
    event.wait 方法时就会阻塞，如果“Flag”值为True，那么event.wait 方法时便不再阻塞。
    clear：将“Flag”设置为False
    set：将“Flag”设置为True

    控制这个属性的值
　　　　set()　　将这个属性的值改成True
　　　　clear()　将这个属性的值改成False
　　　　is_set()  判断当前的属性是否为True

    python线程的事件用于主线程控制其他线程的执行，事件主要提供了三个方法 set、wait、clear。
    事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行
"""
import time
import random
from multiprocessing import Process, Event


def traffic_light(e):
    print('\033[31m红灯亮\033[0m')
    while 1:
        if e.is_set():
            time.sleep(2)
            print('\033[31m红灯亮\033[0m')
            e.clear()
        else:
            time.sleep(2)
            print('\033[32m绿灯亮\033[0m')
            e.set()


def car(e, i):
    if not e.is_set():
        print('car %s 在等待' % i)
        e.wait()
    print('car %s 通过了' % i)


if __name__ == '__main__':
    e = Event()
    p = Process(target=traffic_light, args=(e,))
    p.daemon = True
    p.start()
    p_lst = []
    for i in range(20):
        time.sleep(random.randrange(0, 3, 2))
        p = Process(target=car, args=(e, i))
        p.start()
        p_lst.append(p)
    for p in p_lst:
        p.join()
