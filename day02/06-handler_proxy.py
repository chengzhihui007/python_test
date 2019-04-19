import urllib.request


def handler_proxy():
    url = "https://blog.csdn.net/anonymous_qsh/article/details/79349068"
    proxy = {"http":"49.86.180.166:8888"}
    # urllib.request.build_opener(urllib.request.ProxyHandler(proxy)).open(url).read().decode()

    with open("handler_proxy.html", "w", encoding="UTF-8")as t:
        t.write(urllib.request.build_opener(urllib.request.ProxyHandler(proxy)).open(url).read().decode())

