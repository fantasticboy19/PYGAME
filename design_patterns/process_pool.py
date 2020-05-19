import time
from concurrent.futures import ProcessPoolExecutor

start = time.perf_counter()


# core code: if the task is io-bound, we can use multi_thread to solve the problem, but if the task is
# computing-bound, and owing to the GIL,the applying of multi_thread is not working
def compute_bound():
    print('start to compute')
    # emulate the process of computing
    time.sleep(100)
    print('computing is done')


with ProcessPoolExecutor() as executor:
    # the implement is like the thread_pool as ahead
    pass

finish = time.perf_counter()
print('total time is {}'.format(finish - start))
