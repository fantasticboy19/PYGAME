import itertools
import time
import concurrent
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor

def do_something(seconds):
    print(f'start to sleep {seconds} something fun!')
    time.sleep(seconds)
    return 'this is done!'

t1 = time.perf_counter()

with ThreadPoolExecutor() as executor:
    # results = [executor.submit(do_something, second) for second in [1, 2, 3, 4, 5]]
    # for result in concurrent.futures.as_completed(results):
    #     print(result.result())
    results = executor.map(do_something, [1, 2, 3, 4, 5])
    for result in results:
        print(result)

t2 = time.perf_counter()


print('total time consumed is {}'.format(t2-t1))
# # num = itertools.count(start=2, step=-2)
# print(list(itertools.chain('abc', 'def')))
# print(list(map(pow, range(10), itertools.repeat(2))))