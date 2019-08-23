"""
1、join方法
    - 阻塞主进程，等待子进程执行完毕再放开阻塞
"""
import time
import random
from multiprocessing import Process


# # 单个子进程
# def func(index):
#     print("正在发送")
#     time.sleep(random.randint(1, 3))
#     print("发送完毕")
#
#
# if __name__ == "__main__":
#     p = Process(target=func, args=(1, ))
#     p.start()
#     p.join()
#     print("邮件发送完毕")


# 多个子进程
def func(index):
    time.sleep(random.randint(1, 3))
    print('第%s个邮件已经发送完毕' % index)


if __name__ == '__main__':
    p_lst = []
    for i in range(10):
        p = Process(target=func, args=(i,))
        p.start()
        p_lst.append(p)
    for p in p_lst:
        p.join()    # 等待每个子进程执行完毕
    print('10个邮件已经发送完毕')

