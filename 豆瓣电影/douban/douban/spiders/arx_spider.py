import requests
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}

start_urls = [f'https://arxiv.org/search/?query=weyl+superconductor&searchtype=all&abstracts=show&order=-announced_date_first&size=50&start={i*50}' for i in range(20)]
def run():
    for start_url in start_urls:
        res = requests.get(start_url, headers=headers)
        urls = etree.HTML(res.text).xpath('//li/div/p/span/a[1]/@href')
        # get all path of pdf/url
        for url in urls:
            file_name = url.split('/')[-1]
            print(file_name, url)
            res = requests.get(url, headers=headers)
            if not os.path.exists('papers'):
                os.makedirs('papers')
            with open(f'papers/{file_name}.pdf', 'wb') as f:
                f.write(res.content)
                print(f'{file_name} is done')


if __name__ == '__main__':
    run()
