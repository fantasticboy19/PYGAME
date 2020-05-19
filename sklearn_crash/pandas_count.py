import numpy as np
import pandas as pd


data = pd.DataFrame(data={'name': ['jack', 'mary', 'loris'], 'gender': ['male', 'female', 'male']})
data_unique = data['gender'].unique()
data_values = data['gender'].values
# get the iteration of data_values
_data_ier = iter(data_values)

count_dict = {}

# initialize the count_dict
for i in data_unique:
    count_dict[i] = 0

# start to count the gender
for meta in _data_ier:
    if meta in count_dict.keys():
        count_dict[meta] += 1

# display the result

for key, value in count_dict.items():
    print(f'{key} is {value}')



