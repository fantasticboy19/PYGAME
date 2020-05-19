import requests
from lxml import etree
import parsel
start_url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,Python%2B%25E9%25AB%2598%25E7%25BA%25A7,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
response = requests.get(start_url)

# html = etree.HTML(response.text)
# urls = html.xpath('//div[@class="el"]/p/span/a/@href')
selectors = parsel.Selector(response.text)
urls = selectors.xpath('//div[@class="el"]/p/span/a/@href').extract()
print(type(urls))
for url in urls:
    print(url)
    # response_2 = requests.get(url)
    # print(response_2.text)