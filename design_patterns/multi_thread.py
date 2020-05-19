import threading
import time

start = time.perf_counter()


def do_something(sec):
    time.sleep(sec)
    print('do something')


# t1 = threading.Thread(target=do_something, args=())
# t2 = threading.Thread(target=do_something, args=())
# taskes = [t1, t2]

taskes = [threading.Thread(target=do_something, args=(i,)) for i in range(10)]

for task in taskes:
    task.start()
for task in taskes:
    task.join()

finish = time.perf_counter()

print(f'total time consuming is {finish-start}')