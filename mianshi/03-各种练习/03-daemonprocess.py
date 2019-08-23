"""
3、守护进程
    - 主要功能：每隔一段时间就向一台机器汇报自己的状态（程序的报活）
    - 特点：会随着主进程的结束而结束。
"""

import time
from multiprocessing import Process


def func():
    print('子进程 start')
    time.sleep(3)
    print('子进程 end')


if __name__ == '__main__':
    p = Process(target=func)
    p.daemon = True     # 设置p为一个守护进程，必须在start之前完成
    p.start()
    time.sleep(2)
    print('主进程')
