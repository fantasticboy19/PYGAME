import pyjokes
def greet(name):
    print('hello!', name, f'im telling you a joke {pyjokes.get_joke()}')