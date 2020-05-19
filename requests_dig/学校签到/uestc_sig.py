'''

原本是准备用来模拟登陆来自动签到的，结果失败了，具体就是登陆界面填入账号和密码然后就进不去了，估计是被墙了

'''

import requests
from lxml import etree

session = requests.session()

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'gzip,deflate',
    'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'track_cookie_user_id=1d065363-a86b-9b2c-71ce-b800281fb266;track_cookie_session_id=1fb23ecd-dc8e-2f63-9e99-e4474e3d2ce2;UM_distinctid=16e40ea94d6260-0643fa78a94883-645d7c2d-144000-16e40ea94d7417;_ga=GA1.3.872034612.1573025920;zg_did=%7B%22did%22%3A%20%2216f3c48460929c-00228384ee7c1-6a547d2e-144000-16f3c48460a755%22%7D;__utmz=108824541.1578403062.27.8.utmcsr=idas.uestc.edu.cn|utmccn=(referral)|utmcmd=referral|utmcct=/authserver/callback;__utma=108824541.872034612.1573025920.1582186501.1582367636.38;iPlanetDirectoryPro=mWPmFGAvSjroEEo0oeyyNp;MOD_AUTH_CAS=MOD_AUTH_ST-4759-UNbN4ynSHALJzRumvkUa1582519040946-0ONP-cas;route=30dfce7b7500cd543e989b26cda7c8b4;asessionid=bc962225-7950-4c98-9b77-f607803f55b4;zg_=%7B%22sid%22%3A%201582519052081%2C%22updated%22%3A%201582519052090%2C%22info%22%3A%201582519052088%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22eportal.uestc.edu.cn%22%2C%22cuid%22%3A%20%22201922090617%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201582519052081%7D;amp.locale=undefined;JSESSIONID=t_J1mwua5KUNOYYI8thpZ0I11g3JpBgrObmuexyHIBFLK4fMzQZa!1291555699',
    'Host':'eportal.uestc.edu.cn',
    # 'If-Modified-Since':'Sun, 29 Sep 2019 03:50:45 GMT',
    # 'If-None-Match':'"5d902a15-17773"',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/81.0.4044.9Safari/537.36'
}

start_url = 'http://eportal.uestc.edu.cn/new/index.html'
response = session.get(start_url, headers=headers)
response.encoding = response.apparent_encoding

# html = etree.HTML(response.text)
res2 = session.get('http://eportal.uestc.edu.cn/qljfwapp/sys/lwReportEpidemicStu/index.do?t_s=1582523517497&amp_sec_version_=1&gid_=UzRDUnFwSjZlMkI3dSs1TWlaVDRPQVRpOExwWDZiY0VmV1l4aHEraFA4bWpuaDdmRTBZNkdtbEN1QmJObVFwMU1CWkFXVzFPazU3Q2JXNE1VelBrV3c9PQ&EMAP_LANG=zh&THEME=indigo', headers=headers)
print(res2.text)