import threading

class Singleton(object):
    # initialize the lock for the instance to make the singleton sure !
    instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            # cls.instance = object.__new__(cls)
            with cls.instance_lock:
                cls.instance = object.__new__(cls)

        return cls.instance

def task(arg):
    obj = Singleton()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()
