import random
import time
from memory_profiler import profile

def gene_list():
    names = ['jack', 'mary', 'flood', 'jisse', 'pap']
    majors = ['math', 'cs', 'it', 'art', 'Chinese']

    @profile
    def people_list(people_num):
        people = []
        for i in range(people_num):
            person = {
                'id': i,
                'name': random.choice(names),
                'major': random.choice(majors)
            }
            people.append(person)
        return people

    @profile()
    def people_generator(people_num):
        for i in range(people_num):
            person = {
                'id': i,
                'name': random.choice(names),
                'major': random.choice(majors)
            }
            yield person


    t1 = time.process_time()
    people_generator(100000)
    t2 = time.process_time()
    print('total time usage :{}'.format(t2-t1))


class Celsius:
    def __init__(self, temperature1 = 0):
        self._temperature = temperature1

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

one = Celsius()
print(one.temperature)
one.temperature = 20
print(one.temperature)

