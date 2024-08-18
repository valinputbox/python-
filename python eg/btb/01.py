import requests
import execjs
with open("01.js", encoding="utf-8") as f:
    jsdata = f.read()
JS = execjs.compile(jsdata)
apik = JS.call("getApiKey",)

cookies = {
    'aliyungf_tc': '9a0906eae759fbe673b44c341fd8c94caef8acefbe37d499080005a84a44a2d2',
    'devId': '5fd037e3-2141-494e-92a2-5f432776e57b',
    'ok_site_info': '9FjOikHdpRnblJCLiskTJx0SPJiOiUGZvNmIsIiTDJiOi42bpdWZyJye',
    'locale': 'zh_CN',
    'ok-exp-time': '1719983798764',
    'browserVersionLevel': 'v5.6ad2a8e37c01',
    'first_ref': 'https%3A%2F%2Fwww.oklink.com%2Fzh-hans%2Fbtc',
    'okg.currentMedia': 'xl',
    '_monitor_extras': '{"deviceId":"8Q7vCQOYWw-9g1GBjQyZwV","eventId":77,"sequenceNumber":77}',
    'amp_d77757': '5fd037e3-2141-494e-92a2-5f432776e57b...1i1rj78hp.1i1rkkv93.2d.1.2e',
    'traceId': '1020199882905070001',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'app-type': 'web',
    'cache-control': 'no-cache',
    # 'cookie': 'aliyungf_tc=9a0906eae759fbe673b44c341fd8c94caef8acefbe37d499080005a84a44a2d2; devId=5fd037e3-2141-494e-92a2-5f432776e57b; ok_site_info=9FjOikHdpRnblJCLiskTJx0SPJiOiUGZvNmIsIiTDJiOi42bpdWZyJye; locale=zh_CN; ok-exp-time=1719983798764; browserVersionLevel=v5.6ad2a8e37c01; first_ref=https%3A%2F%2Fwww.oklink.com%2Fzh-hans%2Fbtc; okg.currentMedia=xl; _monitor_extras={"deviceId":"8Q7vCQOYWw-9g1GBjQyZwV","eventId":77,"sequenceNumber":77}; amp_d77757=5fd037e3-2141-494e-92a2-5f432776e57b...1i1rj78hp.1i1rkkv93.2d.1.2e; traceId=1020199882905070001',
    'devid': '5fd037e3-2141-494e-92a2-5f432776e57b',
    'ok-verify-sign': 'F56CeFcLbNm5YiBAxdYfPvlyn4s+o1rC8OMEsbYvZLM=',
    'ok-verify-token': '3c2058d4-cac2-40cf-9734-f304e4eaa20e',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.oklink.com/zh-hans/btc/block-list/page/16',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-apikey':apik,
    'x-cdn': 'https://static.oklink.com',
    'x-id-group': '1040199882847660001-c-2',
    'x-locale': 'zh_CN',
    'x-site-info': '9FjOikHdpRnblJCLiskTJx0SPJiOiUGZvNmIsIiTDJiOi42bpdWZyJye',
    'x-utc': '8',
    'x-zkdex-env': '0',
}

params = {
    'offset': '300',
    'limit': '20',
    't': '1719988434223',
}

response = requests.get('https://www.oklink.com/api/explorer/v1/btc/blocks', params=params, cookies=cookies, headers=headers)
print(response.text)