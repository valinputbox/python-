import requests
import execjs
headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cache-ts': '1720338962670',
    'encryption': 'true',
    'language': 'zh',
    'origin': 'https://www.coinglass.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.coinglass.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

params = {
    'sort': '',
    'order': '',
    'keyword': '',
    'pageNum': '1',
    'pageSize': '20',
    'ex': 'all',
}

response = requests.get('https://capi.coinglass.com/api/home/v2/coinMarkets', params=params, headers=headers)
ret=response.json().get("data")
user=response.headers.get("user")
with open("01.js", encoding="utf8") as f:
    jsdata = f.read()
JS = execjs.compile(jsdata)
k = JS.call("test",ret,user)
print(k)