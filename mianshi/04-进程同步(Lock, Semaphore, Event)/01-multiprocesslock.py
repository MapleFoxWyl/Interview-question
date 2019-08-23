"""
1、锁---multiprocess.Lock
　　- 加锁降低了程序的效率，让原来能够同时执行的代码变成顺序执行了，异步变同步的过程
　　- 好处：保证了数据的安全
"""
import time
import json
from multiprocessing import Process, Lock


# 当多个进程使用同一份数据资源的时候，就会引发数据安全或顺序混乱问题。
# 多进程抢占输出资源
def search(person):
    with open('ticket') as f:
        dic = json.load(f)
    time.sleep(0.2)     # 模拟网络延迟
    print('%s查询余票：' % person, dic['count'])


def get_ticket(person):
    with open('ticket') as f:
        dic = json.load(f)
    time.sleep(0.2)     # 模拟网络延迟
    if dic['count'] > 0:
        print('%s买到票了' % person)
        dic['count'] -= 1   # 买到票，数量减1
        time.sleep(0.2)     # 模拟网络延迟
        with open('ticket', 'w') as f:
            json.dump(dic, f)   # 把剩余票数写回文件
    else:
        print('%s没买到票' % person)


def ticket(person):
    search(person)
    lock.acquire()
    get_ticket(person)
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=ticket, args=('person%s' % i,))
        p.start()






















# 为了保证数据的安全
# 在异步的情况下，多个进程有可能同时修改同一份资源
# 就给这个修改的过程加上锁
