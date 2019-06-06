import requests

url = 'https://www.12306.cn'
headers = {
    'User-Agent': 'test'
}
#忽略证书
response = requests.get(url=url,headers=headers,verify=False)
data = response.content.decode()

with open("test.html", "w" , encoding="utf-8")as t:
    t.write(data)