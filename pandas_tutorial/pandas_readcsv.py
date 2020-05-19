import pandas as pd
import numpy as np

path = r'C:\Users\熊宇\Desktop\douban.csv'

def read_scv(path):
    # job_iter = pd.read_csv(path,iterator=True)
    # print(type(job),job)
    return pd.read_csv(path, chunksize=6)


if __name__ == '__main__':
    # douban_iter= read_scv(path)
    # loop = True
    # chunk = []
    # while loop:
    #     try:
    #         chunks = douban_iter.get_chunk(6)
    #         print(chunks)
    #         chunk.append(chunks)
    #     except StopIteration:
    #         print('iteration error happened')
    #         break
    # dp = pd.concat(chunk)
    # print(dp.dtypes)

    # 第二种读取的方式
    douban_iter = read_scv(path)
    for part in douban_iter:
        print(type(part))
        print(part)