import requests
from lxml import etree
import parsel
import json
def val_attr():
    start_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    headers ={
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding':'gzip,deflate,br',
        'accept-language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control':'max-age=0',
        #'cookie':'RK=ndjAVifIvO;ptcz=a2c3b7fa9d604117444cd34c5ea86b8c731dd3b918c9c9bd6dfbbae91e4946f2;pgv_pvid=3160783470;eas_sid=P1z5g7y3p3q8x0Q5Q5N0v8t9n7;pgv_pvi=9015459840;pac_uid=0_b37b5bfb02392;XWINDEXGREY=0;tvfe_boss_uuid=0833e89138ca3f90;LW_uid=M1z5T7m8W4B6U6j8q552e1B8e8;LW_sid=S145k7Z8T416C6Y8g5w4t2O6F2;psrf_qqunionid=547BA4BFACA7DB75FC9C08B359CF9B01;psrf_qqopenid=93E41D28632BDF54D1658825791149C2;psrf_qqaccess_token=74E59D979AEDCEFBD53E33568BBA850A;psrf_qqrefresh_token=29A2B0E2E7E6F96C1F027C46E728F73F;psrf_access_token_expiresAt=1586925394;ptui_loginuin=2444093230;lskey=0001000035e3d21a90227fd1a68dda08bcafe177b673e6319b239db8f0c712d7bb9ebea93c739214e8f940da',
        'referer':'https://news.qq.com/hdh5/feiyanarea.htm',
        'sec-fetch-dest':'document',
        'sec-fetch-mode':'navigate',
        'sec-fetch-site':'same-origin',
        'sec-fetch-user':'?1',
        'upgrade-insecure-requests':'1',
        'user-agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/81.0.4044.9Safari/537.36',
    }

    response = requests.get(start_url, headers=headers)


    data = response.json()['data']
    # print(type(data))
    # json str
    data2 = json.loads(data)
    # print(type(data2))
    # data2 is dict

    china = data2['areaTree'][0]['children']
    # print(china)

    # 获得湖北的人数
    hubei_province = china[0]['children']
    val = []
    attr = []
    # print(hubei_province)
    for part in hubei_province:
        # print('城市:{},确证总数:{}'.format(part['name'], part['total']['confirm']))
        print(type(part))
        val.append(part['total']['confirm'])
        attr.append(part['name']+'市')

    return val, attr


if __name__ == '__main__':
    val_attr()