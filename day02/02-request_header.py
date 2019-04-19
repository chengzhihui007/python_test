import urllib.request


def load_baidu():
    print("load_baidu~")
    url = "http://www.baidu.com/s?wd=123"
    # response = urllib.request.urlopen("http://www.baidu.com/s?wd=123")
    # 创建请求对象
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    # 响应头
    # print(response.headers)
    # 获取请求头信息
    request_headers = request.headers
    print(request_headers)


load_baidu()