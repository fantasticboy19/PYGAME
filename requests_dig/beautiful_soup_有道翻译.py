from bs4 import BeautifulSoup
import requests

#python 爬虫有道翻译
import requests
from bs4 import BeautifulSoup
import json


while True:

    content = input('请输入要查询的单词/词语(输入0退出翻译):')
    if content == '0':
        print('欢迎下次使用!')
        break
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=null'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_ENTER',
        'typoResult': 'true',
        'i': content,
        'ue': 'UTF-8'#设置翻译支持中文

    }


    res = requests.get(url,params = headers)

    print(res.text)

    # soup = BeautifulSoup(res.text, 'lxml')
    #
    # # soup.text is a json str ,like '{"one":1,"two"：2}'
    # # so,we can use json.loads to make it into a dict
    # # print(type(soup.text))
    # jd = json.loads(soup.text)
    # print(type(jd),jd)
    # # jd = <class 'dict'> {'type': 'EN2ZH_CN', 'errorCode': 0, 'elapsedTime': 1, 'translateResult': [[{'src': 'see', 'tgt': '看到'}]]}
    # print('translate result is :')
    # for translate_list in jd['translateResult'][0]:
    #     print(translate_list['tgt'], end=' ')
    # print('\n')


