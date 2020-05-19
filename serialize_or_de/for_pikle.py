import pickle

target_dict = {
    'name': 'jack',
    'age': 24
}

# solution 1
# target = pickle.dumps(target_dict)
# print(target)
# with open('taeget.pickle', 'wb') as f:
#     f.write(target)
#
# # solution 2
# with open('target.txt', 'wb') as f:
#     pickle.dump(target_dict, f)

with open('target.txt','rb') as f:
    re = pickle.load(f)
