import requests
from lxml import etree
from bs4 import BeautifulSoup
import parsel
import csv
from aiohttp import ClientSession
import asyncio

count = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}
start_urls = [f'https://movie.douban.com/top250?start={25*i}&filter=' for i in range(10)]

with open('douban_250.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['name', 'star', 'des']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()
    for start_url in start_urls:
        res = requests.get(start_url, headers=headers)
        print(res.text)
        urls = etree.HTML(res.text).xpath('//div[@class="item"]/div[@class="info"]/div[@class="hd"]/a/@href')

        for url in urls:
            print(f'cur_url is {url}')
            response = requests.get(url, headers=headers)
            urlcc = parsel.Selector(response.text)

            des = urlcc.xpath('//div[@class="indent"]//span[@property="v:summary"]/text()').extract_first().strip()
            star = urlcc.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract_first()
            movie_name = urlcc.xpath('//div[@id="wrapper"]/div[@id="content"]/h1/span[@property="v:itemreviewed"]/text()').extract_first()

            item = {'name': movie_name, 'star': star, 'des': des}
            # print(type(item), item)
            write.writerow(item)
