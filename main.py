import requests
from bs4 import BeautifulSoup

# 定义目标URL
url = "https://www.333uu.org/xiaoshuo/1.html"

# 发送HTTP请求并获取网页内容
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 使用CSS选择器选择要提取的元素
    selected_element = soup.select_one("body > div:nth-child(5) > div.item > div > ul > li:nth-child(1)")
    
    if selected_element:
        # 将选定的元素文本保存到A.txt文件
        with open("A.txt", "w", encoding="utf-8") as file:
            file.write(selected_element.get_text())
    else:
        print("未找到指定元素")
else:
    print("无法访问指定URL")

