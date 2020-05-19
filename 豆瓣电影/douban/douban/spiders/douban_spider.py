# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['www.movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # print(response.text)
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        # }
        urls = response.xpath('//div[@class="item"]/div[@class="info"]/div[@class="hd"]/a/@href').extract()

        for url in urls:
            print(url)
            yield scrapy.Request(url, callback=self.parse2)

    def parse2(self, response):
        # item = DoubanItem()
        print(type(response))
        movie_name = response.xpath('//div[@id="wrapper"]/div[@id="content"]/h1/span[@property="v:itemreviewed"]/text()')
        movie_star = response.xpath('//div[@class="rating_self clearfix"]/strong/text()')
        movie_description = response.xpath('//div[@class="indent"]//span[@property="v:summary"]/text()')
        # item = {
        #     'movie_name': movie_name,
        #     'movie_star': movie_star,
        #     'movie_description': movie_description
        # }
        item = {
            'name': movie_name,
            'star': movie_star,
            'des':  movie_description
        }
        print(item)