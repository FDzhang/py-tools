import requests
from bs4 import BeautifulSoup
import re


cookie={}


# 子页面解析 -----------------------------------------------------
# 替换为你要爬取的网页地址
url = ''  
response = requests.get(url, cookies=cookie)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# 打印页面内容
# print(soup.prettify())
titles = soup.find_all('span', class_='Title text-truncate', limit=1)
div_elements = soup.find_all('div', class_='my-3', limit=4)

# 打印所有找到的 div 元素的文本内容
# for div_element in div_elements:
#     print(div_element.text)

# 子页面解析 -----------------------------------------------------


# 文件写入 -----------------------------------------------------
# 创建一个空的文件
file = open('output.txt', 'a', encoding='utf-8')

for title in titles:
    file.write(title.text)

# 遍历 div_elements 变量，并将每个 div 元素的文本内容写入到文件
for div_element in div_elements:
    text = re.sub(' +', ' ', div_element.text)
    text = re.sub(r"\n", ' ', text)
    file.write(text)

file.write('\n')

# 关闭文件
file.close()
# 文件写入 -----------------------------------------------------

print("sub page success!!!")