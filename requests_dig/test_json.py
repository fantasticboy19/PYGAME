import json
import requests
from bs4 import BeautifulSoup

# with open('first.json', 'r') as f:
#     data = json.load(f)
#     data['city'] = 'wuhan'
#
# with open('second.json', 'a') as f2:
#     json.dump(data, f2)
# data = {
#     'name': 'jack',
#     'age': 24
# }
# response = requests.get('http://httpbin.org/get', params=data)
# print(response.text)
# print(type(response.content))


# response = requests.get("https://github.com/favicon.ico")
#
# print(type(response.content))
# with open('githu.ico', 'wb') as f:
#     f.write(response.content)

# import requests
#
# url = 'http://httpbin.org/cookies'
# cookies = {'testCookies_1': 'Hello_Python3', 'testCookies_2': 'Hello_Requests'}
# # 在Cookie Version 0中规定空格、方括号、圆括号、等于号、逗号、双引号、斜杠、问号、@，冒号，分号等特殊符号都不能作为Cookie的内容。
# r = requests.get(url, cookies=cookies)
# print(r.json())
# import requests
#
# response = requests.get('https://www.12306.cn')
# print(response.text)
# print(response.status_code)

