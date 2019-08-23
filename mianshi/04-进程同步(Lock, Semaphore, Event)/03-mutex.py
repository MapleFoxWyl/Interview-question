from multiprocessing import Process, Lock

# 互斥锁
lock = Lock()
lock.acquire()
print('456')
lock.acquire()
print('123')
# 只打印456，123不打印