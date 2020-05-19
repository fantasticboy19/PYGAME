import requests
from lxml import etree
# from bs4 import BeautifulSoup
import parsel
import csv
from aiohttp import ClientSession
import asyncio

count = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}
start_url = 'https://movie.douban.com/top250'
res = requests.get(start_url, headers=headers)

urls = etree.HTML(res.text).xpath('//div[@class="item"]/div[@class="info"]/div[@class="hd"]/a/@href')

# with open('douban.csv', 'w', newline='',encoding='utf-8') as f:
#     fieldnames = ['name', 'star', 'des']
#     write = csv.DictWriter(f, fieldnames=fieldnames)
#     write.writeheader()

    # for url in urls:
        # print(f'current url is {url}')
        # response = requests.get(url, headers=headers)
        # # urls = etree.HTML(response.text)
        # urlc = parsel.Selector(response.text)
        # des = urlc.xpath('//div[@class="indent"]//span[@property="v:summary"]/text()').extract_first().strip()
        #
        # star = urlc.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract_first()
        #
        # movie_name = urlc.xpath('//div[@id="wrapper"]/div[@id="content"]/h1/span[@property="v:itemreviewed"]/text()').extract_first()
        #
        # item = {'name': movie_name, 'star': star, 'des': des}
        # # print(type(item), item)
        # write.writerow(item)

async def req(url, headers, write):
    async with ClientSession() as session:
        async with session.get(url,headers=headers) as response:
            response_html = await response.text()
            print(response_html)
            urlcc = parsel.Selector(response_html)

            des = urlcc.xpath('//div[@class="indent"]//span[@property="v:summary"]/text()').extract_first().strip()
            star = urlcc.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract_first()
            movie_name = urlcc.xpath('//div[@id="wrapper"]/div[@id="content"]/h1/span[@property="v:itemreviewed"]/text()').extract_first()

            item = {'name': movie_name, 'star': star, 'des': des}
            # print(type(item), item)
            write.writerow(item)

def run():
    tasks = []
    with open('douban2.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['name', 'star', 'des']
        write = csv.DictWriter(f, fieldnames=fieldnames)
        write.writeheader()
        for url in urls:
            task = req(url, headers, write)
            tasks.append(task)
        loop.run_until_complete(asyncio.wait(tasks))
        # loop.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run()