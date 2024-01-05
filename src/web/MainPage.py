import requests
from bs4 import BeautifulSoup
import re


cookie={}


# 主页面解析 -----------------------------------------------------
main_url=''

response = requests.get(main_url, cookies=cookie)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())
# datas = soup.find_all('div', class_='datashow')

# for data in datas:
#     print(data.text)

# print("main page success!!!")
