import numpy as np

from scipy.stats import ttest_ind

x1 = np.random.normal(2.3, 0.8, 1000)
y1 = np.random.normal(2.3, 0.8, 1000)



def test(x, y):
    return ttest_ind(x, y)

if __name__ == '__main__':
    test(x1,y1)