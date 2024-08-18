import time

import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://bz.zzzmh.cn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://bz.zzzmh.cn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'size': 24,
    'current': 2,
    'sort': 0,
    'category': 0,
    'resolution': 4,
    'color': 0,
    'categoryId': 0,
    'ratio': 0,
}

response = requests.post('https://api.zzzmh.cn/v2/bz/v3/getData', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"size":24,"current":2,"sort":0,"category":0,"resolution":0,"color":0,"categoryId":0,"ratio":0}'
#response = requests.post('https://api.zzzmh.cn/v2/bz/v3/getData', headers=headers, data=data)
ret=response.json().get("data").get("list")
for date in ret:
    i=date.get("i")
    t=date.get("t")
    id_num=i+str(t)+"9"
    url="https://api.zzzmh.cn/v2/bz/v3/getUrl/"+id_num
    res=requests.get(url,headers=headers)

    with open(f"img/{id_num}.jpg","wb")as f:
        f.write(res.content)
        print(f"{id_num}下载成功")

# print(response.text)
# print(ret)