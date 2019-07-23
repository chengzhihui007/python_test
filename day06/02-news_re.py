import re
import requests


url = 'http://news.baidu.com/'
headers = {
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
}
#response.text 不太准确 转码全靠猜
data = requests.get(url,headers=headers).content.decode('utf-8')
#正则解析数据
#每个新闻的titile,url
pattern = re.compile('<a href="(.*)" target="_blank" mon="(.*?)">(.*)</a>')
#pattern = re.compile('<a(.*?)></a>',re.S)
result = pattern.findall(data)
print(result)
# with open('02news.html', 'w', encoding='utf-8')as t:
#     t.write(data)