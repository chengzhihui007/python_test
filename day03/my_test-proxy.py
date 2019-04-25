import urllib.request


def proxy_test():
    #创建用户名密码
    userName = "alibaba"
    password = "mytest"
    proxy_url = "127.0.0.1：8080"
    proxy_manage = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    proxy_manage.add_password(None,proxy_url,userName,password)
    handler = urllib.request.HTTPBasicAuthHandler(proxy_manage)
    oppener = urllib.request.build_opener(handler)
    response = oppener.open("http://www.baidu.com/s?wd=123")
    data = response.read().decode()
    with open("test.html", "w", encoding="utf-8")as t:
        t.write(data)


proxy_test()
