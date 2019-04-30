import requests
import json

url = "https://api.github.com/user"
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)"
}
#这个网址返回的内容不是html 而是标准的json
response = requests.get(url,headers=headers)
# #str
# data = response.text
# #str -> dict
# data_dict = json.loads(data)

# json() 自动将json 字符串 转换成Python dict list
data = response.json()
print(data['message'])