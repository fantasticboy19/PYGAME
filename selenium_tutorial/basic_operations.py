from selenium import webdriver

def run():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'track_cookie_user_id=1d065363-a86b-9b2c-71ce-b800281fb266;track_cookie_session_id=1fb23ecd-dc8e-2f63-9e99-e4474e3d2ce2;UM_distinctid=16e40ea94d6260-0643fa78a94883-645d7c2d-144000-16e40ea94d7417;_ga=GA1.3.872034612.1573025920;zg_did=%7B%22did%22%3A%20%2216f3c48460929c-00228384ee7c1-6a547d2e-144000-16f3c48460a755%22%7D;__utmz=108824541.1578403062.27.8.utmcsr=idas.uestc.edu.cn|utmccn=(referral)|utmcmd=referral|utmcct=/authserver/callback;__utma=108824541.872034612.1573025920.1582186501.1582367636.38;iPlanetDirectoryPro=mWPmFGAvSjroEEo0oeyyNp;MOD_AUTH_CAS=MOD_AUTH_ST-4759-UNbN4ynSHALJzRumvkUa1582519040946-0ONP-cas;route=30dfce7b7500cd543e989b26cda7c8b4;asessionid=bc962225-7950-4c98-9b77-f607803f55b4;zg_=%7B%22sid%22%3A%201582519052081%2C%22updated%22%3A%201582519052090%2C%22info%22%3A%201582519052088%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22eportal.uestc.edu.cn%22%2C%22cuid%22%3A%20%22201922090617%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201582519052081%7D;amp.locale=undefined;JSESSIONID=t_J1mwua5KUNOYYI8thpZ0I11g3JpBgrObmuexyHIBFLK4fMzQZa!1291555699',
        'Host': 'eportal.uestc.edu.cn',
        # 'If-Modified-Since':'Sun, 29 Sep 2019 03:50:45 GMT',
        # 'If-None-Match':'"5d902a15-17773"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/81.0.4044.9Safari/537.36'

    }
    cookies = {
        'route': '9d4f6df72dd80e37818ed3f3a5777081',
        'EMAP_LANG':'zh',
        'THEME': 'indigo',
        '_WEU': 'fBImrIt32LquUUWXJCXyCKc8Vwu_6AmfKG8n7p1m*sr8o*_GNTN5SKZPRLNxVtgQGI03o9VJCeqXLFOUQBbjJkvxjPrcximb_4yWS5TGsYO_JclYSvLnUlc3XSndf1JpU5Q*_xg5kA*8efLw64o27c..',
        'UM_distinctid': '16e40ea94d6260-0643fa78a94883-645d7c2d-144000-16e40ea94d7417',
        '_ga': 'GA1.3.872034612.1573025920',
        'zg_did': '%7B%22did%22%3A%20%2216f3c48460929c-00228384ee7c1-6a547d2e-144000-16f3c48460a755%22%7D',
        '__utmz': '108824541.1578403062.27.8.utmcsr=idas.uestc.edu.cn|utmccn=(referral)|utmcmd=referral|utmcct=/authserver/callback',
        '__utma': '108824541.872034612.1573025920.1582186501.1582367636.38',
        'iPlanetDirectoryPro': 'BciRcUdobabGjsse3GtweP',
        'MOD_AUTH_CAS': 'MOD_AUTH_ST-5497-41ytHeZtiMymFDIhYoUk1582522362520-husd-cas',
        'route': '07f03ed1ed6e496f5392b5b234387177',
        'asessionid': '9a235b02-d355-4382-b9af-1dffda1fbf66',
        'amp.locale': 'undefined',
        'zg_': '%7B%22sid%22%3A%201582523521511%2C%22updated%22%3A%201582523521522%2C%22info%22%3A%201582519052088%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22eportal.uestc.edu.cn%22%2C%22cuid%22%3A%20%22201922090617%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201582523521511%7D',
        'JSESSIONID': 'OAN1wb2tRRnvMcIZt9eraZtRCcfV26MxmhlAB_Mp8gI-Ymc_Dghz!1444055450'
    }
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

    driver = webdriver.Chrome(executable_path='E:\conda\envs\profile_version\chromedriver.exe')
    # driver.get('https://idas.uestc.edu.cn/authserver/login?service=http%3A%2F%2Feportal.uestc.edu.cn%2Flogin%3Fservice%3Dhttp%3A%2F%2Feportal.uestc.edu.cn%2Fnew%2Findex.html')
    # driver.get('http://eportal.uestc.edu.cn/new/index.html')
    driver.get('http://eportal.uestc.edu.cn/new/index.html')
    driver.add_cookie(cookies)
    driver.get('http://eportal.uestc.edu.cn/qljfwapp/sys/lwReportEpidemicStu/index.do?t_s=1582523517497&amp_sec_version_=1&gid_=UzRDUnFwSjZlMkI3dSs1TWlaVDRPQVRpOExwWDZiY0VmV1l4aHEraFA4bWpuaDdmRTBZNkdtbEN1QmJObVFwMU1CWkFXVzFPazU3Q2JXNE1VelBrV3c9PQ&EMAP_LANG=zh&THEME=indigo#/dailyReport')

    # driver.find_element_by_id("ampHasNoLogin").click()
    # driver.find_element_by_id('username').send_keys('201922090617')
    # driver.find_element_by_id('password').send_keys('y50024019923677*')
    # driver.find_element_by_xpath('//*[@id="casLoginForm"]/p[4]/button').submit()
    driver.refresh()


if __name__ == '__main__':
    run()