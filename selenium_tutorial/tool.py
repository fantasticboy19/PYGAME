cookie_str = '''track_cookie_user_id=1d065363-a86b-9b2c-71ce-b800281fb266; 
track_cookie_session_id=1fb23ecd-dc8e-2f63-9e99-e4474e3d2ce2; 
UM_distinctid=16e40ea94d6260-0643fa78a94883-645d7c2d-144000-16e40ea94d7417; _ga=GA1.3.872034612.1573025920; 
zg_did=%7B%22did%22%3A%20%2216f3c48460929c-00228384ee7c1-6a547d2e-144000-16f3c48460a755%22%7D; 
__utmz=108824541.1578403062.27.8.utmcsr=idas.uestc.edu.cn|utmccn=(
referral)|utmcmd=referral|utmcct=/authserver/callback; 
__utma=108824541.872034612.1573025920.1582186501.1582367636.38; iPlanetDirectoryPro=BciRcUdobabGjsse3GtweP; 
MOD_AUTH_CAS=MOD_AUTH_ST-5497-41ytHeZtiMymFDIhYoUk1582522362520-husd-cas; route=07f03ed1ed6e496f5392b5b234387177; 
asessionid=9a235b02-d355-4382-b9af-1dffda1fbf66; amp.locale=undefined; 
zg_=%7B%22sid%22%3A%201582523521511%2C%22updated%22%3A%201582524173287%2C%22info%22%3A%201582519052088%2C
%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C
%22referrerDomain%22%3A%20%22eportal.uestc.edu.cn%22%2C%22cuid%22%3A%20%22201922090617%22%2C%22zs%22%3A%200%2C%22sc
%22%3A%200%2C%22firstScreen%22%3A%201582523521511%7D; 
JSESSIONID=eD91zLowZAIbrAw3jjnlzk8XcC-rV-liklqRJxRpe_QTNDWDz6WZ!1444055450 
'''
cookie_list = cookie_str.split(';')
for i in cookie_list:
    print(i)