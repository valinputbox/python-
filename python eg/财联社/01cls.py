import requests
import execjs

cookies = {
    'HWWAFSESID': 'ebfbe769ce05322da3',
    'HWWAFSESTIME': '1721132480390',
    'hasTelegraphNotification': 'on',
    'hasTelegraphRemind': 'on',
    'hasTelegraphSound': 'on',
    'vipNotificationState': 'on',
    'Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e': '1720076684,1721132484',
    'Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e': '1721132484',
    'HMACCOUNT': '96FE2327DCA6F9F5',
    'tfstk': 'fnOSOBab1uqWwW8fxT3V1odLKq1Ib3GaAy_pSeFzJ_C8vkLO0Q5F4eIBdiL9U6uka9CB-3KCK4jFvMteJLuq_f8kr6fpAclZ_Ag3_99CJTIKJZQKQNNL0f8krrCKbclZ_JwebSgCvHBRMrQGDWedJHEAkibhJuQLwqTAmwCdJ9BdMsQ1SuIdvb_KfZDO2UgXr1PosbxHyiN6oIQ8bMlGDWQDZaBW_EjfPaOfPTsO30c51QK2JQRlnxeftEJ6ApKt08SJCNtfQLi_NhtlJe_pVf41DQTBGTv475Lfdg9vwtaL9E8veOpBV0wl2L-fIZBYRfb2biLkwKg3DUKNV_QA3f36k9p2ZOArD719IU5yphn4Ugp1Jgl__GtPAJafIW_fbqgbKJ5ZDPKvSzfXgTQcuIujluZVeZbfbqgbKJXRoZWSlqZ70',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=utf-8',
    # 'Cookie': 'HWWAFSESID=ebfbe769ce05322da3; HWWAFSESTIME=1721132480390; hasTelegraphNotification=on; hasTelegraphRemind=on; hasTelegraphSound=on; vipNotificationState=on; Hm_lvt_fa5455bb5e9f0f260c32a1d45603ba3e=1720076684,1721132484; Hm_lpvt_fa5455bb5e9f0f260c32a1d45603ba3e=1721132484; HMACCOUNT=96FE2327DCA6F9F5; tfstk=fnOSOBab1uqWwW8fxT3V1odLKq1Ib3GaAy_pSeFzJ_C8vkLO0Q5F4eIBdiL9U6uka9CB-3KCK4jFvMteJLuq_f8kr6fpAclZ_Ag3_99CJTIKJZQKQNNL0f8krrCKbclZ_JwebSgCvHBRMrQGDWedJHEAkibhJuQLwqTAmwCdJ9BdMsQ1SuIdvb_KfZDO2UgXr1PosbxHyiN6oIQ8bMlGDWQDZaBW_EjfPaOfPTsO30c51QK2JQRlnxeftEJ6ApKt08SJCNtfQLi_NhtlJe_pVf41DQTBGTv475Lfdg9vwtaL9E8veOpBV0wl2L-fIZBYRfb2biLkwKg3DUKNV_QA3f36k9p2ZOArD719IU5yphn4Ugp1Jgl__GtPAJafIW_fbqgbKJ5ZDPKvSzfXgTQcuIujluZVeZbfbqgbKJXRoZWSlqZ70',
    'Pragma': 'no-cache',
    'Referer': 'https://www.cls.cn/telegraph',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'os': 'web',
    'sv': '7.7.5',
    'app': 'CailianpressWeb',

}
with open("./cls.js",encoding="utf-8")as f:
    cls=f.read()
sign=execjs.compile(cls).call("clw",params)
params["sign"]=sign

response = requests.get('https://www.cls.cn/v3/depth/banner', params=params, cookies=cookies, headers=headers)
print(response.text)