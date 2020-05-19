
class base:
    tasks = []

    # def add_task(self, name):
    #     base.tasks.append(name)

    @classmethod
    def add_task(cls, name):
        cls.tasks.append(name)
        print(type(cls) == type(base))
        print(id(cls) == id(base))


base1 = base()
base2 = base()

base1.add_task('cat')
base2.add_task('dog')
print('base.tasks={},base1.tasks={},base2.tasks={}'.format(base.tasks, base1.tasks, base2.tasks))