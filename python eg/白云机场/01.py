import requests
import execjs
cookies = {
    'HMACCOUNT': '96FE2327DCA6F9F5',
    'Hm_lpvt_0effb2f651854e064f7d24a159e08bd5': '1722431880',
    'Hm_lpvt_38ddcda5baa19a6a899f6f3f7471381a': '1722431880',
    'Hm_lpvt_483eff6efca2ca9bff48af354895a36f': '1722431880',
    'Hm_lpvt_783519365e6df848bd882229527a15bc': '1722431881',
    'Hm_lpvt_e9e5e5ffd5a25d3f4d7e1466807ef7b7': '1722431880',
    'Hm_lvt_0effb2f651854e064f7d24a159e08bd5': '1719898278',
    'Hm_lvt_38ddcda5baa19a6a899f6f3f7471381a': '1719898278',
    'Hm_lvt_483eff6efca2ca9bff48af354895a36f': '1719898278',
    'Hm_lvt_783519365e6df848bd882229527a15bc': '1719898279',
    'Hm_lvt_e9e5e5ffd5a25d3f4d7e1466807ef7b7': '1719898278',
    'JSESSIONID': 'ZoQstbFMtbWXco_i9BvTkL6rSZ16qen040NmC3GE',
    'Hm_lvt_38ddcda5baa19a6a899f6f3f7471381a': '1719898278,1719992445,1721632952,1722431880',
    'Hm_lpvt_38ddcda5baa19a6a899f6f3f7471381a': '1722431880',
    'HMACCOUNT': '96FE2327DCA6F9F5',
    'Hm_lvt_0effb2f651854e064f7d24a159e08bd5': '1719898278,1719992445,1721632952,1722431880',
    'Hm_lpvt_0effb2f651854e064f7d24a159e08bd5': '1722431880',
    'Hm_lvt_e9e5e5ffd5a25d3f4d7e1466807ef7b7': '1719898278,1719992445,1721632952,1722431880',
    'Hm_lpvt_e9e5e5ffd5a25d3f4d7e1466807ef7b7': '1722431880',
    'Hm_lvt_483eff6efca2ca9bff48af354895a36f': '1719898278,1719992445,1721632952,1722431880',
    'Hm_lpvt_483eff6efca2ca9bff48af354895a36f': '1722431880',
    'Hm_lvt_783519365e6df848bd882229527a15bc': '1719898279,1719992445,1721632952,1722431881',
    'Hm_lpvt_783519365e6df848bd882229527a15bc': '1722431881',
    'JSESSIONID': 'wik4BALGxnlOoHmBe900KgV-HjZ_LlrbuRjFxiuz',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'HMACCOUNT=96FE2327DCA6F9F5; Hm_lpvt_0effb2f651854e064f7d24a159e08bd5=1722431880; Hm_lpvt_38ddcda5baa19a6a899f6f3f7471381a=1722431880; Hm_lpvt_483eff6efca2ca9bff48af354895a36f=1722431880; Hm_lpvt_783519365e6df848bd882229527a15bc=1722431881; Hm_lpvt_e9e5e5ffd5a25d3f4d7e1466807ef7b7=1722431880; Hm_lvt_0effb2f651854e064f7d24a159e08bd5=1719898278; Hm_lvt_38ddcda5baa19a6a899f6f3f7471381a=1719898278; Hm_lvt_483eff6efca2ca9bff48af354895a36f=1719898278; Hm_lvt_783519365e6df848bd882229527a15bc=1719898279; Hm_lvt_e9e5e5ffd5a25d3f4d7e1466807ef7b7=1719898278; JSESSIONID=ZoQstbFMtbWXco_i9BvTkL6rSZ16qen040NmC3GE; Hm_lvt_38ddcda5baa19a6a899f6f3f7471381a=1719898278,1719992445,1721632952,1722431880; Hm_lpvt_38ddcda5baa19a6a899f6f3f7471381a=1722431880; HMACCOUNT=96FE2327DCA6F9F5; Hm_lvt_0effb2f651854e064f7d24a159e08bd5=1719898278,1719992445,1721632952,1722431880; Hm_lpvt_0effb2f651854e064f7d24a159e08bd5=1722431880; Hm_lvt_e9e5e5ffd5a25d3f4d7e1466807ef7b7=1719898278,1719992445,1721632952,1722431880; Hm_lpvt_e9e5e5ffd5a25d3f4d7e1466807ef7b7=1722431880; Hm_lvt_483eff6efca2ca9bff48af354895a36f=1719898278,1719992445,1721632952,1722431880; Hm_lpvt_483eff6efca2ca9bff48af354895a36f=1722431880; Hm_lvt_783519365e6df848bd882229527a15bc=1719898279,1719992445,1721632952,1722431881; Hm_lpvt_783519365e6df848bd882229527a15bc=1722431881; JSESSIONID=wik4BALGxnlOoHmBe900KgV-HjZ_LlrbuRjFxiuz',
    # 'Nonce': '7f5bef06-95bb-459c-a9ff-c7d6ad1eedd9',
    'Origin': 'https://www.baiyunairport.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.baiyunairport.com/flight/dep',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # 'Signature': 'j4EJkChlGPQMGrBn7mMWhOf2foKfKG5F4U6MJGyx34zPuvVjXFKA0iDpWiOGZq/tWew6DmpNWWqTwWzBVbEnh9hUPzCNSnADrhsPpYOtPuVK1FJMXeTTlCAcMUZgpJmP6NjM+KF+RhDgimV85ptIbnKmkff/W+6XE9Brv040xyTwZ4c/a1fcJQ3i8lYrk0uiV6lIgHBJVsE84ccAL5FdEXplQeix8ei3Ofz0ZWOwlHVMV+UCCBVhg8bmTJHxZvymh1ZYnbDel1Pg8dCb+xqL3NLmmbo6HQ2wpCxuLcqhxmb5DiSJeHYQa7nngCLsObHMJipPhXu942VWcDpy3Cnolw==',
    # 'Timestamp': '1722431903584',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'locale': 'zh_CN',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'type': '1',
    'terminal': '',
    'day': 0,
    'depOrArr': '1',
    'pageNum': 3,
    'pageSize': 15,
}
with open("sign.js",encoding="utf-8") as f:
        sign=f.read()
JS = execjs.compile(sign)
b = JS.call("sign",json_data)
print(b)

headers['Timestamp']=str(b['timestamp'])
headers['Nonce']=b['nonce']
headers['Signature']=b['signature']
response = requests.post(
    'https://www.baiyunairport.com/byairport-flight/flight/list',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"type":"1","terminal":"","day":0,"depOrArr":"1","pageNum":2,"pageSize":15}'
#response = requests.post('https://www.baiyunairport.com/byairport-flight/flight/list', cookies=cookies, headers=headers, data=data)
print(response.text)