import requests
import execjs
cookies = {
    'Hm_lvt_4b4ce93f1c92033213556e55cb65769f': '1719835603,1719983032',
    'ct_m_dvc_id': '8fe1328ea0dd9564e99c840c6892964e',
    'ct_m_sid2': '1719986024187-OlXXzquQl4',
    'ct_m_pvid': '1',
    'sid1': '1720005309808-FC39752E55F73723F8FA547DB17EC4BA',
    'sid2': '1720005309808-FC39752E55F73723F8FA547DB17EC4BA',
    'Hm_lpvt_4b4ce93f1c92033213556e55cb65769f': '1720005357',
    'pvid': '4',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'Hm_lvt_4b4ce93f1c92033213556e55cb65769f=1719835603,1719983032; ct_m_dvc_id=8fe1328ea0dd9564e99c840c6892964e; ct_m_sid2=1719986024187-OlXXzquQl4; ct_m_pvid=1; sid1=1720005309808-FC39752E55F73723F8FA547DB17EC4BA; sid2=1720005309808-FC39752E55F73723F8FA547DB17EC4BA; Hm_lpvt_4b4ce93f1c92033213556e55cb65769f=1720005357; pvid=4',
    'Origin': 'https://m.ctyun.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://m.ctyun.cn/wap/main/auth/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'x-riskdevicesign': '5e57e6044ab63eee783fc58c96455df8',
}

params = {
    'referrer': 'wap',
    'mainVersion': '300031500',
    'comParam_curTime': '1720005374317',
    'comParam_seqCode': '8D4078189EFB033445DD4F576D5EAD9E',
    'comParam_signature': '6b98f1ce75925ccdea3187af9ed71d0e',
    'isCheck': 'true',
    'locale': 'zh-cn',
}
with open("./01 tyy.js",encoding="utf-8") as f:
        jsdata=f.read()
Js=execjs.compile(jsdata)
b=Js.call("",)
data = {
    'userName': '1123123344@126.com',
    'password': 'fpID3TAyw3yfCgkMrJ9sjA==',
}

response = requests.post('https://m.ctyun.cn/account/login', params=params, cookies=cookies, headers=headers, data=data)
print(response.text)