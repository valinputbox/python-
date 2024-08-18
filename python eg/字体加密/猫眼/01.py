import requests
import re

from fontTools.ttLib import TTFont
import ddddocr
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

from lxml import etree

cookies = {
    '_lxsdk_cuid': '190d91a1dd62-09bfc0dd263125-26001e51-149c48-190d91a1dd7c8',
    'uuid_n_v': 'v1',
    'uuid': 'A52E2FE047F211EFA42B35DCA6CA47BF805B0DA11F7E4F809D322CA76DA89FE2',
    '_csrf': '4481e815c798a5e959173eb8f644873a6b3123ce806446109d832df249efcd52',
    '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
    '_lxsdk': 'A52E2FE047F211EFA42B35DCA6CA47BF805B0DA11F7E4F809D322CA76DA89FE2',
    'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2': '1721629296',
    'HMACCOUNT': '96FE2327DCA6F9F5',
    'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2': '1721629588',
    '__mta': '151827078.1721629295974.1721629583570.1721629588682.6',
    '_lxsdk_s': '190d91a1dd8-140-0b3-ff2%7C%7C14',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': '_lxsdk_cuid=190d91a1dd62-09bfc0dd263125-26001e51-149c48-190d91a1dd7c8; uuid_n_v=v1; uuid=A52E2FE047F211EFA42B35DCA6CA47BF805B0DA11F7E4F809D322CA76DA89FE2; _csrf=4481e815c798a5e959173eb8f644873a6b3123ce806446109d832df249efcd52; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk=A52E2FE047F211EFA42B35DCA6CA47BF805B0DA11F7E4F809D322CA76DA89FE2; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1721629296; HMACCOUNT=96FE2327DCA6F9F5; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1721629588; __mta=151827078.1721629295974.1721629583570.1721629588682.6; _lxsdk_s=190d91a1dd8-140-0b3-ff2%7C%7C14',
    'Pragma': 'no-cache',
    'Referer': 'https://www.maoyan.com/films?sortId=2',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'showType': '2',
}

response = requests.get('https://www.maoyan.com/films', params=params, cookies=cookies, headers=headers)
#（1）下载woff文件
data=response.text
path=re.findall(',url\("(.*?woff)"',response.text)[0]
# print(path)
woff_url="https:"+path
res=requests.get(woff_url)
with open("font.woff","wb")as f:
    f.write(res.content)
#（2）提取字体映射
def convert_cmap_to_image(cmap_code, font_path):
    img_size = 1024
    img = Image.new("1", (img_size, img_size), 255)  # 创建一个黑白图像对象
    draw = ImageDraw.Draw(img)  # 创建绘图对象
    font = ImageFont.truetype(font_path, img_size)  # 加载字体文件
    character = chr(cmap_code)  # 将 cmap code 转换为字符

    bbox = draw.textbbox((0, 0), character, font=font)  # 获取文本在图像中的边界框
    width = bbox[2] - bbox[0]  # 文本的宽度
    height = bbox[3] - bbox[1]  # 文本的高度
    draw.text(((img_size - width) // 2, (img_size - height) // 2), character, font=font)  # 绘制文本，并居中显示
    return img
def extract_text_from_font(font_path):
    font = TTFont(font_path)  # 加载字体文件
    font.saveXML("xxx.xml")
    ocr = ddddocr.DdddOcr(beta=True, show_ad=False)  # 实例化 ddddocr 对象
    font_map = {}
    for cmap_code, glyph_name in font.getBestCmap().items():
        bytes_io = BytesIO()
        image = convert_cmap_to_image(cmap_code, font_path)  # 将字体字符转换为图像
        image.save(bytes_io, "PNG")
        text = ocr.classification(bytes_io.getvalue())  # 图像识别
        image.save(f"./imgs/{text}.png", "PNG")  # 保存图像
        print(f"Unicode码点：{cmap_code} - Unicode字符:{glyph_name}，识别结果：{text}")
        font_map[glyph_name.replace("uni","&#x").lower()] = text

    return font_map
font_file_path = "font.woff"
font_map=extract_text_from_font(font_file_path)
print("font_map:::",font_map)
#（3）字体解密
for k, v in font_map.items():
    data=data.replace(k+";",v)
#(4)解析数据
html_Data = etree.HTML(data)
div_list = html_Data.xpath('//dl[@class="movie-list"]//dd')

for v in div_list:
    try:
        title = v.xpath(f'./div[2]/a/text()')[0]
        stone_font = v.xpath(f'./div[3]/span/text()')[0]

        print("title:", title)
        print("stone_font:", stone_font)
        print("*" * 30)
    except IndexError:
        continue