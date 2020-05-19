# -*- coding: utf-8 -*-
import scrapy
from jobSpider.items import JobspiderItem

class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/020000,000000,0000,00,9,99,Python%2520%25E9%25AB%2598%25E7%25BA%25A7,2,\
    1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&l\
    onlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']
    def parse(self, response):
        selectors = response.xpath('//div[@class="el"]')
        for selector in selectors:
            url = selector.xpath('./p/span/a/@href').get(default='')
            if url:
                print(url)
                yield scrapy.Request(url, callback=self.parseDetail)

    def parseDetail(self, response):
        corporation_name = response.xpath('//p[@class="cname"]/a/@title').get(default='')
        post_name = response.xpath('//div[@class="cn"]/h1/@title').get(default='')
        post_wage = response.xpath('//div[@class="cn"]/strong/text()').get(default='')

        # items = {
        #     '公司': corporation_name,
        #     '岗位': post_name,
        #     '工资': post_wage
        # }
        items = JobspiderItem(name=corporation_name,post=post_name,wage=post_wage)
        # self.result.append(items)
        print(items)
        yield items



