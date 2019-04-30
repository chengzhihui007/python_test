# 安装 第三方模块 requests
# pip  install requests


import requests

class RequestSpider(object):
    def __init__(self):
        url = "https://www.baidu.com/s"
        params = {"wd":"大宝剑"}
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)"
        }
        self.response = requests.get(url, headers=headers,params=params)

    def run(self):

        data = self.response.content
        text = self.response.text
        #1.获取请求头
        request_headers = self.response.request.headers
        print(request_headers)
        #2.获取响应头
        response_headers = self.response.headers
        print(response_headers)
        # #3.相应状态码
        code = self.response.status_code
        print(code)
        #4.请求的cookie
        request_cookie = self.response.request._cookies
        print(request_cookie)
        # #5.相应的coolie
        response_cookie = self.response.cookies
        print(response_cookie)
        with open("request_user.html", "w", encoding="UTF-8")as t:
            t.write(text)

        #发送post 和添加参数
        #requests.post(url,data=(参数{}),json=(参数))

RequestSpider().run()