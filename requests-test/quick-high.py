#高级用法
import json

import  requests;

#会话对象
#跨请求保持一下cookie
# s= requests.Session()
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)
#设置默认值，缺省数据
# s = requests.Session()
# s.auth = ('user', 'pass')
# s.headers.update({'x-test': 'true'})
# #both 'x-test' and 'x-test2' are sent
# r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
# print(r.text)
#就算使用了会话，方法级别的参数也不会被夸请求保存。下面的例子智慧和第一个请求发送cookie,而非第二个
# s = requests.Session()
# r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
# print(r.text)
# r = s.get('http://httpbin.org/cookies')
# print(r.text)
#会话还可以用做前后文管理器
# with requests.Session() as s:
#     s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
#

#请求与相应对象
# r = requests.get('http://www.baidu.com')
# print(r.text)
# print(r.request.headers)

#准备的请求
# from requests import Request, Session
# s = Session()
# req = Request('GET',url,data=data,headers=header)
# prepped = req.prepare()
# #do something with prepped.body
# #do something with prepped.headers
# resp = s.send(prepped,stream=stream,verify=verify,proxies=proxies,cert=cert,timeout=timeout)
# print(resp.status_code)

#SSL证书验证
# s = requests.get('https://reqeustb.in',)
# print(s.text)
#https请求需要设置SSL
# s = requests.get('https://github.com', verify=True)
# print(s.status_code)
#为verify传入CA_BUNDLE文件的路径，或者包含可信任CA证书文件的文件夹路径：
# s = requests.get('https://github.com',verify='/path/to/certfile')
# print(s.text)
#或者将其保持在会话中：
# s = requests.Session()
# s.verify = '/path/to/certfile'
#ps: 如果verify 设为文件夹路径，文件夹必须通过OpenSSL提供的c_rehash工具处理。
#如果verify设置为False,Requests 也能忽略对SSL证书的验证。
# s= requests.get('https://kennethreitz.org', verify=False)
# print(s.status_code)


#客户端证书
# s = requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.key'))
# print(s)

#CA证书
#响应体内容工作流
# tarball_url = 'https://github.com/kennethreitz/requests/tarball/master'
# r = requests.get(tarball_url,stream=True)
# if int(r.headers['content-length']) < TOO_LONG:
#     content = r.content
# print(r.text)
# with requests.get('http://httpbin.org/get', stream=True) as r:
#     print(r.text)

#保持活动状态(持久连接)


#流式上传
# with open('holidaytemplate.xlsx') as f:
#     requests.post('http://some.url/streamed', data=f)


#块编码请求
# def gen():
#     yield 'hi'
#     yield 'there'
# requests.post('http://some.url/chunked', data=gen())


#post多个分块编码的文件
# url = 'http://httpbin.org/post'
# multiple_files = [('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
#                   ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
# r = requests.post(url,files=multiple_files)
# print(r.text)


#事件挂钩
# def print_url(r, *args, **kwargs):
#     print(r.url)
# #hooks = dict(response=print_url)
# s = requests.get('http://httpbin.org', hooks=dict(response=print_url()))
# print(s.text)


#自定义身份验证
# from requests.auth import  AuthBase
#
# class PizzaAuth(AuthBase):
#     """Attaches HTTP Pizza Authentication to the given Request object."""
#     def _init_(self,username):
#         #setup any auth-related data here
#         self.username = username
#
#     def _call__(self,r):
#         #modify and return the  request
#         r.headers['X-Pizza'] = self.username
#         return r
#
# s = requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))
# print(s.text)

#流式请求
# import json
# import requests
# r = requests.get('http://httpbin.org/stream/20', stream=True)
#
# # for line in r.iter_lines():
# #     #filter out keep-alive new lines
# #     if line:
# #         decoded_line = line.decode('utf-8')
# #         print(json.loads(decoded_line))
#
# #当使用decode_unicode=True 时，需要提供一个回退编码方式，以防服务器没有提供默认编码，导致错误：
# if r.encoding is None:
#     r.encoding = 'utf-8'
#
# for line in r.iter_lines(decode_unicode=True):
#     if line:
#         print(json.loads(line))


#代理
# proxies = {
#     'http' : 'http://117.191.11.110:8080',
#     'http' : 'http://123.206.200.63:1080'
# }
#
# s = requests.get('http://example.org', proxies=proxies)
# print(s.text)
#若你的代理需要使用HTTP Basic Auth,可以使用http://user:password@host/语法：
# proxies = {'http': 'http://user:pass@10.10.1.10:3128'}
# #若为某个特定的连接方式或者主机设置代理，使用scheme://hostname作为key
# proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}


# #SOCKS
# # pip install requests[socks]
# proxies = {
#     'http:': 'sock5://user:pass@host:port',
#     'https': 'socks5://user:pass@host:port'
# }

#HTTP动词:GET/OPTIONS/HEAD/POST/PUT/PATCH/DELETE。
# r = requests.get('https://api.github.com/repos/requets/requests/git/commit/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
# print(r.status_code)
# print(requests.codes.ok)
# print(r.headers['content-type'])
# print(r.json().keys())
# print(r.json()[u'documentation_url'])
# verbs = requests.options(r.url)
# print(verbs.status_code)
# verbs2 = requests.options('http://www.baidu.com')
# print(verbs2.headers['Connection'])
r = requests.get('https://api.github.com/requests/kennethreitz/requests/issues/482')
print(r.status_code)
issue = json.loads(r.text)
print(issue[u'documentation_url'])
print(issue['documentation_url'])
r = requests.get(r.url+u'/documentation_url')
print(r.status_code)