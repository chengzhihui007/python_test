import urllib.request
import urllib.parse


def load_baidu():
    url = "http://www.baidu.com/s?"
    params = {"wd":"大宝剑"}
    final_url= url+urllib.parse.urlencode(params)
    print(final_url)
    proxys = {"ip":"192.168.1.1"}
    request = urllib.request.Request(final_url)
    request.add_header("a","aaa")
    print(request.headers)
    # response = urllib.request.urlopen(request)
    handler = urllib.request.ProxyHandler(proxys)
    opener = urllib.request.build_opener(handler)
    # print(opener.open(request))
    response = opener.open(request);
    data = response.read().decode()
    # print(urllib.request.build_opener(handler))
    # print(data)
    with open("a.html", "w", encoding="UTF-8")as t:
        t.write(data)


load_baidu()