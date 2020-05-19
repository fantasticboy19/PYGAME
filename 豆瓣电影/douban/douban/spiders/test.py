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
start_url = 'https://arxiv.org/pdf/1901.01520'
res = requests.get(start_url, headers=headers)
with open('one.pdf', 'wb') as f:
    f.write(res.content)