import requests

url = ""
cookie={}

fileName='response4.json'
logName='log1.txt'

for i in range(308, 309):
    payload = {'pid':'310000','cid':'0','page':str(i),'ontype':'0','keywords':'0'}

    response = requests.post(url, cookies=cookie, data=payload)

    # 检查请求是否成功
    if response.status_code == 200:
        # 将响应内容写入文件
        with open(fileName, "a", encoding="utf-8") as file:
            file.write(response.text)

        log = "page: "+ str(i)+ "请求成功，响应已写入文件 response.json"
        with open(logName, "a", encoding="utf-8") as file:
            file.write(log)
            file.write('\n')
        print(log)
    else:
        log = "page: "+ str(i)+ f"请求失败，状态码: {response.status_code}"
        with open(logName, "a", encoding="utf-8") as file:
            file.write(log)
            file.write(response.text)
            file.write('\n')
        print(log)
        print(response.text)

print("all success!!!")