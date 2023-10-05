import requests
from bs4 import BeautifulSoup

url = "https://www.333uu.org/xiaoshuo/1/"

# 发送GET请求获取网页内容
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 使用CSS选择器获取所需元素
    element = soup.select_one("body > div:nth-child(5) > div.item > div > ul > li:nth-child(1)")

    # 打印元素的文本内容
    if element:
        print(element.text)
    else:
        print("未找到指定元素")
else:
    print("请求失败")
