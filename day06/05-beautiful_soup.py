 #https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story"><!--...--></p>
"""

# #1.转类型
# #默认bs4会调用系统中lxml的解析库 警告提示
# #主动设置bs4的解析库
# soup = BeautifulSoup(html_doc, 'lxml')
#
# #2.格式化输出 补全
# result = soup.prettify()
# print(result)

#1.转类型 bs4.BeautifulSoup
# soup = BeautifulSoup(html_doc,'lxml')
 #
 # #2.解析数据
 #
 # #Tag 标签对象 bs4.element.Tag
 # result = soup.head
 # #bs4.element.Comment
 # result_p = soup.p.string
 # result = soup.a
 # print(type(result_p))
 # print(result_p)
 # #内容 bs4.element.NavigableString
 # result = soup.a.string
 # #print(type(result))
 # #属性
 # result = soup.a['href']
 # print(type(soup))

#1 转类型
soup = BeautifulSoup(html_doc, 'lxml')

#2 通用解析方法

# find-返回符合查询条件的第一个标签
result = soup.find(name='p')
result = soup.find(attrs={"class": "title"})
result = soup.find(text='Tillie')
result = soup.find(
    name='p',
    attrs={'class': 'story'}
)
#find_all-list(标签对象)
result = soup.find_all(name='p')
result = soup.find_all('a', limit=1)[0]
result = soup.find_all(attrs={'class': 'sister'})

#select_one--css选择器
result = soup.select_one('.sister')
#select--css选择器
result = soup.select('.sister')
#id选择器
result = soup.select('#one')
#后代选择器
result = soup.select('head title')
#主选择器
result = soup.select('title,.title')
#属性选择器
result = soup.select('a[id="link3"]')

#标签包裹的内容--list
result= soup.select('b')[0].get_text()
#标签的属性
result = soup.select('#link1')[0].get('href')
print(result)
