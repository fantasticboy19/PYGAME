from concurrent.futures import ThreadPoolExecutor
import time

start = time.perf_counter()


def do_something(sec):
    print('do something')
    time.sleep(sec)
    print('Done')

def download(url):
    print('start to download')
    # star to download
    time.sleep(2)

    print(
        'download is done'
    )

with ThreadPoolExecutor() as executor:
    secs = [1, 2, 3, 4, 5]
    results = [executor.map(do_something, secs)]
    # urls = ['www','www']
    # results = [executor.map(download, urls)]

finish = time.perf_counter()

print(f'total time consuming is {finish-start}')
