import string
import urllib.request


def load_baidu():
    url = "http://www.baidu.com/s?"
    # param = "wd=大宝剑"
    params = {"wd":"大宝剑"}
    final_url = url +urllib.parse.urlencode(params)
    print(final_url)
    request = urllib.request.Request(final_url)
    response = urllib.request.urlopen(final_url)
    data = response.read().decode()
    with open("data.html", "w", encoding="UTF-8")as t:
        t.write(data)


load_baidu()