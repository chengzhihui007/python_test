import urllib.request
import urllib.parse
import string


def my_test():
    print("start~")
    url = "http://www.baidu.com/s?"
    param = "wd=大宝剑"
    params = {"wd":"大宝剑2","wd2":"ddd"}
    print(urllib.parse.quote(param,safe=string.printable))
    print(urllib.parse.urlencode(params))
    with open("my_test_even04.html", "w", encoding="UTF-8")as t:
        t.write(urllib.request.urlopen(url+urllib.parse.quote(param,safe=string.printable)).read().decode())

    print("second~")
    with open("my_test_even04-02.html", "w", encoding="UTF-8")as t:
        t.write(urllib.request.urlopen(url+urllib.parse.urlencode(params)).read().decode())
    print("end.")


my_test()
