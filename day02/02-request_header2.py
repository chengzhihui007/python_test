import urllib.request


def load_baidu_test():
    print("start~")
    url = "http://www.baidu.com/s?"
    param = "wd=123"
    headers = {"abc-bca":"test_aaa"}
    request = urllib.request.Request(url+param,headers=headers)
    # 请求头添加信息
    request.add_header("bbb","test_bbb")
    # 获取完整url
    full_url = request.get_full_url()
    print(full_url)
    response = urllib.request.urlopen(request)
    with open("a.html", "w", encoding="UTF-8")as t:
        t.write(response.read().decode())
    print(request.headers)
    print(request.get_header("Abc-bca"))
    # print(response.headers)


load_baidu_test()