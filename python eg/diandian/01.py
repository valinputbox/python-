import json
import re
import time

import requests
import execjs
cookies = {
    'deviceid': '3033db08ffd66499e8ec2405d81a314',
    '_ga': 'GA1.1.1616145683.1719571195',
    'Hm_lvt_4b46d92b8c2be1622e347873de8ada00': '1719573370',
    'Hm_lvt_c420cc498e4250baa6114afe2947045e': '1719573370',
    'Hm_lvt_e1382854e68f4d69f837bb54a6d1e22f': '1719573370',
    'activityTime': '1719676799999',
    'Qs_lvt_404253': '1719571191%2C1719639235%2C1719797295%2C1719833549',
    'Qs_pv_404253': '3762297964070126600%2C3553642394876238300%2C1937083736969195800%2C1668429143272921300%2C2522032448183722500',
    '_ga_GVCWL6PNZ2': 'GS1.1.1719833531.5.1.1719836313.0.0.0',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'deviceid=3033db08ffd66499e8ec2405d81a314; _ga=GA1.1.1616145683.1719571195; Hm_lvt_4b46d92b8c2be1622e347873de8ada00=1719573370; Hm_lvt_c420cc498e4250baa6114afe2947045e=1719573370; Hm_lvt_e1382854e68f4d69f837bb54a6d1e22f=1719573370; activityTime=1719676799999; Qs_lvt_404253=1719571191%2C1719639235%2C1719797295%2C1719833549; Qs_pv_404253=3762297964070126600%2C3553642394876238300%2C1937083736969195800%2C1668429143272921300%2C2522032448183722500; _ga_GVCWL6PNZ2=GS1.1.1719833531.5.1.1719836313.0.0.0',
    'Origin': 'https://app.diandian.com',
    'Pragma': 'no-cache',
    'Referer': 'https://app.diandian.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'language': 'zh',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
rse=requests.get('https://app.diandian.com/',cookies=cookies,headers=headers)
reg=r"u:\{.*?\}"
ret=re.search(reg,rse.text).group(0)[2:-5]+"}"
ret=ret.replace("s:",'"s":').replace("k:",'"k":').replace("l:",'"l":')
# print(ret)
d=json.loads(ret)
# print(d,type(d))
# print(reponse.text)
params = {
    'app_id': 'y21ulux1r7mwra1',
    'country_id': '75',
    'market_id': '1',
    'device_id': '1',
    'start_time': str(int(time.time())),
    'end_time':str(int(time.time())+40000),
    # 'k': 'W0ZWUUNSUncEEFpHVlFDUlN2ARpaR1BTC1lVNV5dEkYVUR8cFiEDAExRTldCXVd5BBhbQ1BOVE1NJFYATFFOSQRaSzVBTRhYAQcEBBYpRk1FFhcW',
}
with open("01.js", encoding="utf8") as f:
    jsdata = f.read()
JS = execjs.compile(jsdata)
k = JS.call("date_dict",params,d)
params["k"]=k
response = requests.get('https://api.diandian.com/pc/app/v1/user/favorite/app', params=params, cookies=cookies, headers=headers)
print(response.text)