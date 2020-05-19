from collections import namedtuple
from collections import OrderedDict
import pprint

def test_tuple():
    my_tuple = namedtuple('my_tuple', ['name', 'age'])
    t = my_tuple(name='jack', age=24)
    print(f'content is : {t.name} is {t.age}, and the doc is {t.__doc__}')


def test_OrderedDict():
    ordered_dict = OrderedDict()
    ordered_dict['name'] = 'jack'
    ordered_dict['age'] = '24'
    ordered_dict['salary'] = '240000/month'
    print(ordered_dict)


if __name__ == '__main__':
    test_tuple()
    test_OrderedDict()
