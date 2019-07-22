#高级用法

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
#to be continue ...
#http://2.python-requests.org/zh_CN/latest/user/advanced.html


