"""
2、第二种开启进程的方法
    - 以继承Process类的形式开启进程的方式
"""
import os
import time
from multiprocessing import Process


# class MyProcess(Process):
#     def run(self):
#         print("子进程：", os.getpid(), os.getppid())
#
#
# if __name__ == "__main__":
#     p = MyProcess()
#     p.start()
#     print('主进程：', os.getpid())


# 给子进程传参
class MyProcess(Process):
    def __init__(self, arg):
        super().__init__()
        self.arg = arg
    def run(self):
        time.sleep(1)
        print('子进程: ', os.getpid(), os.getppid(), self.arg)


# if __name__ == '__main__':
#     # 开启单个子进程
#     p = MyProcess('参数')
#     p.start()   # 开启一个子进程，让这个子进程执行run方法
#     p.join()
#     print('主进程：', os.getpid())

# 开启多个子进程
if __name__ == '__main__':
    for i in range(10):
        p = MyProcess("参数%s"%i)
        p.start()
        p.join()
    print('主进程：', os.getpid())


