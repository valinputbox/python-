import json

import requests
import execjs
cookies = {
    'wd_guid': '2ef606b8-2006-4507-8eff-f00c8ecc81b3',
    'historyState': 'state',
    '__c': '1721026613',
    '__g': '-',
    '__l': 'l=%2Fwww.kanzhun.com%2Fsearch%3FpageNum%3D1%26query%3Dpython%26type%3D5&r=',
    'Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e': '1720341125,1721026613',
    'HMACCOUNT': '96FE2327DCA6F9F5',
    'wbrwsid': '44430818',
    '__a': '55122925.1720341122.1720341122.1721026613.11.2.6.11',
    'Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e': '1721026782',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    # 'cookie': 'wd_guid=2ef606b8-2006-4507-8eff-f00c8ecc81b3; historyState=state; __c=1721026613; __g=-; __l=l=%2Fwww.kanzhun.com%2Fsearch%3FpageNum%3D1%26query%3Dpython%26type%3D5&r=; Hm_lvt_1f6f005d03f3c4d854faec87a0bee48e=1720341125,1721026613; HMACCOUNT=96FE2327DCA6F9F5; wbrwsid=44430818; __a=55122925.1720341122.1720341122.1721026613.11.2.6.11; Hm_lpvt_1f6f005d03f3c4d854faec87a0bee48e=1721026782',
    'href': 'https://www.kanzhun.com/search?pageNum=1&query=python&type=5',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.kanzhun.com/search?pageNum=1&query=python&type=5',
    'reqsource': 'fe',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceid': '7ebdeae8-af92-4cf4-8b06-68abfe8f69a5',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

date_n = {"query":"python",
          "cityCode":101020100,
          "salaryId":"",
          "experienceId":"",
          #可以更改页码
          "pageNum":1,
          "limit":15}
n=json.dumps(date_n)
with open("01mod.js", encoding="utf8") as f:
    jsdata = f.read()
JS = execjs.compile(jsdata)
b = JS.call("enc",n)
params = {
    'b': b[0],
    'kiv': b[1],
}

response = requests.get('https://www.kanzhun.com/api_to/search/job.json', params=params, cookies=cookies, headers=headers)


b = JS.call("dec",response.text,b[1])
print(b)