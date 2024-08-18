import requests
import execjs
import requests

cookies = {
    'acw_tc': '2760778d17195691282643103e489fe749be91d77106b278714a0d63445368',
    'Hm_lvt_b966fe201514832da03dcf6cbf25b8a2': '1719569130',
    'Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2': '1719569130',
    'ssxmod_itna': 'Qqmx0DnDyiYmqD5GHeGdI3r4+r61DcD7wuKhqhA4Pm9KDskGbDSxGKidDqxBmet4YKA7GDYqGDZSBDtGzl44w7kGBBp+m2iZ8G+h=xCPGnDBFxoTDeeND5xGoDPxDeDADYERDAqiOD7qDFIdX/lLtDm4GWIqGfDDoDY8U9DitD4qDBjOQDKqGgITmqjuDD0uDW=7GBWuGPhCQ3gwTZKDR=97tDjuTD/4mz=7tQZP7qeebk2=2H8qGyCKGulwXxdwu3jw0Vbm4ezExoK+GoW8wxfRxeWaeemDx4R+GxYxmaDgCWLfYtAiC2xDWk0Dki4+G4eiDD==',
    'ssxmod_itna2': 'Qqmx0DnDyiYmqD5GHeGdI3r4+r61DcD7wuKhqhA4PexikUkqYKDl66Ojxj+lTsh=YKWq2tqM3CuYRxeoD8HnOcDOCib+w9xAPztd4EMaePon13r812p69GAzamjQlUq//Wn123P9PfmDEIgl4d0+ueyQRLX3wrPxqdX8SEMAM6UC0=zlfN+ibtQgShuerpmegh8YPhthd3eDrE4pookjcLZ0MIoMBF4OMdCq=bCwwGhMP0gK0IZecg8iSHh9Gcue8XtehcfNmYUDOux8UkUIOv=rD4X1K01WGeXxWQiWGasr8aUYDLuKx9BhRlRI8+=lRO8bMSyttqClF2lvrYDejxc9x43qb8KxRWxDKqCA7m25zTAK4IeTxx9OAmk4ch0aH8FOCOs8HvURPMhGUhWloc/RcBrRbbtubbU9/t7=zBWlBDkK//+WKWADYbZbK6eED9H9exb2nb3YKeF90vfbNW9WDFCQ+LC3kT+5vnOmPOHiNW0QPhZA8KvRubpbHMXBPz2ebly/G7rdvWbdOsBgGCda5vRANuKBF+qXRcIq4RFeYL40R4YMjRY/7fW0yFV0S0hyCgx9IQtvZQjHNm5ySat5PNfdD07IieG0Dgm8i7TRGcosggCGN5Yj9xeo54+8jkk+BeaXMZBMM7zCsgrrk+rai7MliZpVXjPeD7=DYKU8DtYbBsqqlQq+oYHIitcHebMlCXrgCq50=7DqAoDhq+fWPTBoCbd2kY4B+jYDD===',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'acw_tc=2760778d17195691282643103e489fe749be91d77106b278714a0d63445368; Hm_lvt_b966fe201514832da03dcf6cbf25b8a2=1719569130; Hm_lpvt_b966fe201514832da03dcf6cbf25b8a2=1719569130; ssxmod_itna=Qqmx0DnDyiYmqD5GHeGdI3r4+r61DcD7wuKhqhA4Pm9KDskGbDSxGKidDqxBmet4YKA7GDYqGDZSBDtGzl44w7kGBBp+m2iZ8G+h=xCPGnDBFxoTDeeND5xGoDPxDeDADYERDAqiOD7qDFIdX/lLtDm4GWIqGfDDoDY8U9DitD4qDBjOQDKqGgITmqjuDD0uDW=7GBWuGPhCQ3gwTZKDR=97tDjuTD/4mz=7tQZP7qeebk2=2H8qGyCKGulwXxdwu3jw0Vbm4ezExoK+GoW8wxfRxeWaeemDx4R+GxYxmaDgCWLfYtAiC2xDWk0Dki4+G4eiDD==; ssxmod_itna2=Qqmx0DnDyiYmqD5GHeGdI3r4+r61DcD7wuKhqhA4PexikUkqYKDl66Ojxj+lTsh=YKWq2tqM3CuYRxeoD8HnOcDOCib+w9xAPztd4EMaePon13r812p69GAzamjQlUq//Wn123P9PfmDEIgl4d0+ueyQRLX3wrPxqdX8SEMAM6UC0=zlfN+ibtQgShuerpmegh8YPhthd3eDrE4pookjcLZ0MIoMBF4OMdCq=bCwwGhMP0gK0IZecg8iSHh9Gcue8XtehcfNmYUDOux8UkUIOv=rD4X1K01WGeXxWQiWGasr8aUYDLuKx9BhRlRI8+=lRO8bMSyttqClF2lvrYDejxc9x43qb8KxRWxDKqCA7m25zTAK4IeTxx9OAmk4ch0aH8FOCOs8HvURPMhGUhWloc/RcBrRbbtubbU9/t7=zBWlBDkK//+WKWADYbZbK6eED9H9exb2nb3YKeF90vfbNW9WDFCQ+LC3kT+5vnOmPOHiNW0QPhZA8KvRubpbHMXBPz2ebly/G7rdvWbdOsBgGCda5vRANuKBF+qXRcIq4RFeYL40R4YMjRY/7fW0yFV0S0hyCgx9IQtvZQjHNm5ySat5PNfdD07IieG0Dgm8i7TRGcosggCGN5Yj9xeo54+8jkk+BeaXMZBMM7zCsgrrk+rai7MliZpVXjPeD7=DYKU8DtYbBsqqlQq+oYHIitcHebMlCXrgCq50=7DqAoDhq+fWPTBoCbd2kY4B+jYDD===',
    'Pragma': 'no-cache',
    'Referer': 'https://ctbpsp.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'type__1017': 'eqGxy7G=DtemqAKD=D/YnhOeTtGQKd+i74D',
}

response = requests.get(
    'https://ctbpsp.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/3',
    params=params,
    cookies=cookies,
    headers=headers,
)



# execjs.compile(open("01.js").read()).call("decryptByDES",response.text)