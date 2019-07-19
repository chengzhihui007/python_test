import requests

# r=requests.get("https://api.github.com/events")
#
# print(r)
#
# r= requests.post("http://httpbin.org/post",data = {'key':'value'});
# print(r)
#
# r = requests.put('http://httpbin.org/put', data={'key':'value'})
# print(r)
#
# r = requests.delete('http://httpbin.org/delete')
# print(r)
#
# r = requests.head('http://httpbin.org/get')
# print(r)
#
# r = requests.options('http://httpbin.org/get')
# print(r)

#传递URL参数
# payload = {'key1':'value1', 'key2':'value2'}
# r = requests.get('http://httpbin.org/get', params=payload)
# print(r.url)
# payload2 = {'key1':'value1', 'key2': ['value2','value3']}
# r2 = requests.get('http://httpbin.org/get', params=payload2)
# print(r2.url)

#响应内容
# r = requests.get('https://api.github.com/evnets')
# print(r.text)
# #改变编码集
# print(r.encoding)
# r.encoding = 'ISO-8859-1'
# print(r.encoding)
#二进制响应内容
# print(r.content)
#二进制之自动解码gzip和deflate传输编码的相应数据。
# r = requests.get('http://aibilloss.17got.com/oss/file/aibill/upload/j1560318323920/2019-07-15/uaKEYee1osg9GQ9FRPo.png')
# from PIL import  Image
# from io import BytesIO
# i = Image.open(BytesIO(r.content))
#保存图片
# with open("b.png","wb") as wr:
#     for date in r.iter_content(5):
#         wr.write(date)
#json响应内容
# print(r.raise_for_status())
# print(r.status_code)
#print(r.json())

#原始相应内容
# r = requests.get('http://aibilloss.17got.com/oss/file/aibill/upload/j1560318323920/2019-07-15/uaKEYee1osg9GQ9FRPo.png', stream = True)
# print(r.raw)
# print(r.raw.read(10))
#将文本 保存到文件
# with open("a.txt",'wb') as fd:
#     for chunk in r.iter_content(1):
#         fd.write(chunk)

#定制请求头
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
# r = requests.get(url,headers=headers)
# print(r.json())


#更加复杂的POST请求
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)

#或者这样也阔以
# payload = (('key1', 'value1'),('key2', 'value2'))
# r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)

#例如，githubapi v3 接受编码为json的 post/patch数据：
# import json
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# r = requests.post(url, data=json.dumps(payload))
# print(r.text)

#post 一个多部分编码(Multipart-Encoded)的文件
# url = 'http://httpbin.org/post'
# files = {'file': open('holidaytemplate.xlsx', 'rb')}
# r= requests.post(url,files=files)
# print(r.text)
#例如,显式地设置文件名，文件类型和请求头
# url = 'http://httpbin.org/post'
# files = {'file':('holidaytemplate.xlsx', open('holidaytemplate.xlsx','rb'), 'application/vnd.ms-excel', {'Expires' :'0'})}
# r = requests.post(url, files=files)
# print(r.text)
#如果你想，你也可以发送作为文件来接收的字符串：
# url = 'http://httpbin.org/post'
# files = {'file': ('holidaytemplate.xlsx', 'some,data,to,send\nanother,row,to,send\n')}
# r = requests.post(url, files=files)
# print(r.text)

#相应状态码
# r = requests.get('http://httpbin.org/get')
# print(r.status_code)
#
# bad_r = requests.get('http://httpbin.org/status/404')
# print(bad_r.status_code)
# print(bad_r.raise_for_status())


#响应头
# r = requests.get('http://httpbin.org/get')
# print(r.headers['Content-Type'])
# print(r.headers.get('content-type'))

#Cookie
# url = 'http://example.com/some/cookie/setting/url'
# r = requests.get(url)
# print(r.cookies)

# 要想发送你的cookies到服务器，可以使用cookies参数
# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r= requests.get(url,cookies=cookies)
# print(r.text)

#Cookie的返回对象为RequestsCookieJar,
jar = requests.cookies.RquestsCookieJar()

#http://2.python-requests.org/zh_CN/latest/user/quickstart.html
#to be continue ...




