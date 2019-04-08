import urllib.request
import urllib.parse
import string


def my_test():
    url = "http://www.baidu.com/s?"
    params1 = "大美女啊aaa"
    params2 = {
        "wd": "啊啊"
    }
    print(urllib.parse.quote(params1))
    print(urllib.parse.urlencode(params2))
    response = urllib.request.urlopen(url).read().decode()
    print(response)
    with open("my_test.html", "w", encoding="UTF-8")as test:
        test.write(urllib.request.urlopen(url+urllib.parse.urlencode(params2)).read().decode())


my_test()
