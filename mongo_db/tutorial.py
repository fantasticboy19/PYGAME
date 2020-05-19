import os

import pymongo

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client.test
col = db.worker

work1 = {
    'id': 1,
    'name': 'jack',
    'habit': 'soccer'
}
work2 = {
    'id': 2,
    'name': 'rose',
    'habit': 'soccer'
}
work3 = {
    'id': 3,
    'name': 'kristine',
    'habit': 'soccer'
}

result = col.insert_many([work1, work2, work3])
print(result)

path = os.path.abspath(__file__)
print(f'origin abspath is {__file__},later is {os.path.abspath(__file__)}')
