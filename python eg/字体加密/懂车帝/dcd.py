from fontTools.ttLib import TTFont
import ddddocr
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import requests

def convert_cmap_to_image(cmap_code, font_path):
    img_size = 1024
    img = Image.new("1", (img_size, img_size), 255)  # 创建一个黑白图像对象
    draw = ImageDraw.Draw(img)  # 创建绘图对象
    font = ImageFont.truetype(font_path, int(img_size*0.7))  # 加载字体文件
    character = chr(cmap_code)  # 将 cmap code 转换为字符

    bbox = draw.textbbox((0, 0), character, font=font)  # 获取文本在图像中的边界框
    width = bbox[2] - bbox[0]  # 文本的宽度
    height = bbox[3] - bbox[1]  # 文本的高度
    draw.text(((img_size - width) // 2, (img_size - height) // 7), character, font=font)  # 绘制文本，并居中显示
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
        # image.save(f"./imgs{text}.png", "PNG")  # 保存图像
        # print(f"Unicode码点：{cmap_code} - Unicode字符:{glyph_name}，识别结果：{text}")
        font_map[hex(cmap_code).replace("0x", r"")] = text

    return font_map
font_file_path = "dcd.woff2"
font_map = extract_text_from_font(font_file_path)
def dcd():
    cookies = {
        'ttwid': '1%7CNFBlORuI0RZCcqI4ynacAaoW30H1kvtISwdMARsczUc%7C1721745812%7C136c1e905b1ab8bf0c9a85175de833e4472aa587ef5296fe3aa5d3cb40874018',
        'tt_webid': '7394841903047607870',
        'tt_web_version': 'new',
        'is_dev': 'false',
        'is_boe': 'false',
        'Hm_lvt_3e79ab9e4da287b5752d8048743b95e6': '1721745813',
        'HMACCOUNT': '96FE2327DCA6F9F5',
        '_gid': 'GA1.2.393318265.1721745814',
        's_v_web_id': 'verify_lyyj05xw_1W6GsSc1_wDzV_4jOT_BgzG_57YQz2orOBP3',
        'city_name': '%E6%89%AC%E5%B7%9E',
        '_ga': 'GA1.1.1359374825.1721745813',
        '_ga_YB3EWSDTGF': 'GS1.1.1721745813.1.1.1721746037.60.0.0',
        'Hm_lpvt_3e79ab9e4da287b5752d8048743b95e6': '1721746038',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'ttwid=1%7CNFBlORuI0RZCcqI4ynacAaoW30H1kvtISwdMARsczUc%7C1721745812%7C136c1e905b1ab8bf0c9a85175de833e4472aa587ef5296fe3aa5d3cb40874018; tt_webid=7394841903047607870; tt_web_version=new; is_dev=false; is_boe=false; Hm_lvt_3e79ab9e4da287b5752d8048743b95e6=1721745813; HMACCOUNT=96FE2327DCA6F9F5; _gid=GA1.2.393318265.1721745814; s_v_web_id=verify_lyyj05xw_1W6GsSc1_wDzV_4jOT_BgzG_57YQz2orOBP3; city_name=%E6%89%AC%E5%B7%9E; _ga=GA1.1.1359374825.1721745813; _ga_YB3EWSDTGF=GS1.1.1721745813.1.1.1721746037.60.0.0; Hm_lpvt_3e79ab9e4da287b5752d8048743b95e6=1721746038',
        'origin': 'https://www.dongchedi.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.dongchedi.com/usedcar/x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'x-forwarded-for': '',
    }

    params = {
        'aid': '1839',
        'app_name': 'auto_web_pc',
    }

    data = '&sh_city_name=全国&page=1&limit=20'.encode()

    response = requests.post(
        'https://www.dongchedi.com/motor/pc/sh/sh_sku_list',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    #{"data":{"has_more":true,"search_sh_sku_info_list":[{"authentication_method":"{"data":{"has_more":true,"search_sh_sku_info_list":[{"authentication_method":"
    info_list=response.json().get("data").get("search_sh_sku_info_list")

    return info_list
def change(code):
    s=""
    for i in code:
        if i != ".":
            i=font_map[repr(i)[3:-1]]
            s+=i
    return s
def change_code(data):
    if data.find("|") != -1:
        a, b = data.split("|")
        return change(a.strip())+change(b.strip())
def main():
    info_list=dcd()
    for  item in info_list:
        d={
            "标题": item.get("title"),
            "品牌": item.get("brand_name"),
            "官方指导价 ": change(item.get("official_price")),
            "售价 ": change(item.get("sh_price")),
            "子标题 ": change_code(item.get("sub_title")),
        }
        print(d)

main()