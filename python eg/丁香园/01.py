import requests
import execjs
import random
import time
cookies = {
    'dxy_da_cookie-id': 'b3eccea06e4e3f1e153dcda1656c39ab1719918403202',
    '_ga': 'GA1.1.1722013624.1719918404',
    'Hm_lvt_5fee00bcc4c092fe5331cc51446d8be2': '1719918404',
    'JUTE_SESSION_ID': '1440242c-2fa2-4c31-b31d-3334318fcbaf',
    'ifVisitOldVerBBS': 'false',
    'Hm_lpvt_5fee00bcc4c092fe5331cc51446d8be2': '1719918463',
    '_ga_LTBPLJJK75': 'GS1.1.1719918403.1.1.1719918465.0.0.0',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=utf-8',
    # 'cookie': 'dxy_da_cookie-id=b3eccea06e4e3f1e153dcda1656c39ab1719918403202; _ga=GA1.1.1722013624.1719918404; Hm_lvt_5fee00bcc4c092fe5331cc51446d8be2=1719918404; JUTE_SESSION_ID=1440242c-2fa2-4c31-b31d-3334318fcbaf; ifVisitOldVerBBS=false; Hm_lpvt_5fee00bcc4c092fe5331cc51446d8be2=1719918463; _ga_LTBPLJJK75=GS1.1.1719918403.1.1.1719918465.0.0.0',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.dxy.cn/bbs/newweb/pc/case/search?keyword=%E6%96%B0%E5%86%A0',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '71fb8ce2f9664cb0a8424320b84082df-bea3beb4d3c9a555-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}
noncestr="".join([str(random.randint(0,9) for _ in range(8))])
timestamp=int(time.time()*1000)

params = {
    'keyword': '新冠',
    'sectionCode': '0',
    'pageSize': '20',
    'pageNum': '1',
    'serverTimestamp':str(timestamp-2) ,
    'timestamp': str(timestamp),
    'noncestr': noncestr,
}
sign_encrty=f'appSignKey=4bTogwpz7RzNO2VTFtW7zcfRkAE97ox6ZSgcQi7FgYdqrHqKB7aGqEZ4o7yssa2aEXoV3bQwh12FFgVNlpyYk2Yjm9d2EZGeGu3&keyword={params["keyword"]}&noncestr={params["noncestr"]}&pageNum={params["pageNum"]}&pageSize={params["pageSize"]}&sectionCode={params["sectionCode"]}&serverTimestamp={params["serverTimestamp"]}&timestamp={params["timestamp"]}'
with open("01.js", encoding="utf-8") as f:
    jsdata = f.read()
JS = execjs.compile(jsdata)
sign = JS.call("u",sign_encrty)
params["sign"]=sign
response = requests.get('https://www.dxy.cn/bbs/newweb/case-bank/page-post-info', params=params, cookies=cookies, headers=headers)
print(response.text)