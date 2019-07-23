import re
from lxml import etree
import requests

url = 'http://news.baidu.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
}
#response.text 不太准确 转码全靠猜
data = requests.get(url,headers=headers).content.decode('utf-8')

#1.转解析类型
xpath_data = etree.HTML(data)
#xpath 语法 1.节点 /
#           2.跨节点： //
#           3.精确的标签：//a[@属性="属性值"]
#           4.标签包裹的内容 text()
#           5.属性：@href
#             xpath--s数据类型--list
#2.调用xpath的方法, 下标是从1 开始；只能取平级关系的标签
result = xpath_data.xpath('/html/head/title//text()')
result = xpath_data.xpath('//a/text()')
result = xpath_data.xpath('//a[@mon="ct=1&a=1&c=top&pn=0"]/text()')
result = xpath_data.xpath('//a[@mon="ct=1&a=1&c=top&pn=0"]/@href')
result = xpath_data.xpath('//li/a/text()')
#print(len(result[0]))
print(result)
# with open('02news.html', 'w', encoding='utf-8')as t:
#     t.write(data)
 