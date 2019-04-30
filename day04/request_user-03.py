#安装第三方模块 reqeusts
# pip install requests

import requests


def  user_request_test():
    url = "http://www.baidu.com"
    response = requests.get(url)
#   content属性返回的类型 是 bytes
    data = response.content.decode("utf-8")
    print(type(data))

#   text 属性 返回的类型是 文本str
    data = response.text
    print(type(data))

user_request_test()
