# np.random.randint(1, 2, (3, 4))

class Method(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print(self.name, 'is', self.age)
        print('*' * 20)
        print(args, kwargs)


if __name__ == '__main__':
    method01 = Method('jack', 24)
    method01(1, 2, 3, a=40)
    input('input a num')
    print('hello world', '|', 'hello guys', end='\n')