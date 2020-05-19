import requests
from lxml import etree
import time

start_time = time.time()

start_url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,Python%2520%25E9%25AB%2598%25E7%25BA%25A7,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
response = requests.get(start_url)
# print(response.status_code, response.encoding, response.apparent_encoding)
# print(response.text)
response.encoding = response.apparent_encoding
res_html = etree.HTML(response.text)
urls = res_html.xpath('//div[@class="el"]/p/span/a/@href')
items = []
for url in urls:
    # print(url)
    response2 = requests.get(url)
    response2.encoding = response2.apparent_encoding
    res2_html = etree.HTML(response2.text)
    corporation_name = res2_html.xpath('//div[@class="cn"]/p[@class="cname"]/a/@title')
    items.append(corporation_name)

end_time = time.time()

print(len(items),items,'total time =',end_time-start_time)