import requests

def test_cookie_and_session():
    start_url = 'https://www.51job.com/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.9 Safari/537.36 '
    }
    print(headers)
    session = requests.session()

    response = session.get(start_url, headers=headers)
    response.encoding = response.apparent_encoding
    print(response.text)
    cookies = response.cookies
    print(cookies.keys(), cookies.values())

    session.get('https://hrawards.51job.com/', headers=headers)
    print(response.cookies.keys(), response.cookies.values())

class Person:
    count = 10
    def __init__(self, name):
        self.name = name

    @property
    def say_myname(self, name_revised='mary'):
        self.name = name_revised
        print(f'im saying ...{self.name}')
    # 进过修饰之后不能传入参数，可以用来写固定的逻辑，返回某一需要的数据即可。

class Work:
    def __init__(self):
        pass


if __name__ == '__main__':
    person = Person('jack')
    person.say_myname
    # error: person.say_myname(parameters)