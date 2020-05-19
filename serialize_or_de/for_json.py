import json



target_dict = {
    'name': 'jack',
    'age': 24
}
# solution 1
# target_dict_tostr = json.dumps(target_dict)
# with open('target.json','w') as f:
#     f.write(target_dict_tostr)

# # solution2
# with open('target2.json','w') as f:
#     json.dump(target_dict, f)

with open('target.json','r') as f:
    result = json.load(f)
print(result)