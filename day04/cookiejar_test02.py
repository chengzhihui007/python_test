import  urllib.request
from http import cookiejar
from urllib import parse

def  cookie_test():
# 1.代码登录
#1.1 登录的网址
    login_url = "https://www.yaozh.com/login"
#     1.2 登录的参数
    login_form_data = {
        "username":"chengzhihui007",
        "pwd":"qwer1234",
        "formhash":"CE3ADF28C5",
        "backurl":"https%3A%2F%2Fwww.yaozh.com%2F"
    }
#     1.3 发送登录请求
    cookie_jar = cookiejar.CookieJar()
#   定义有添加 cookie功能的处理器
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)
#   根据处理器生成 opener
    openner = urllib.request.build_opener(cookie_handler)
#   带着参数 发送post请求
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)"
    }
    login_form_data_url = parse.urlencode(login_form_data).encode("UTF-8")
#   post  参数必须是 bytes
    login_request = urllib.request.Request(login_url,headers=headers,data=login_form_data_url)
#   如果登录成功《cookiejar自动保存cookie
    openner.open(login_request)

#   2.代码带着cookie去访问 个人中心
    center_url = "https://www.yaozh.com/member/"
    center_request = urllib.request.Request(center_url,headers=headers)
    response = openner.open(center_url)
#   bytes -> str
    data = response.read().decode()

    with open("cookiejar.html", "w", encoding="UTF-8")as t:
        t.write(data)


cookie_test()