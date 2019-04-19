import random
import urllib.request

def handler_random_proxy():
    url = "https://jingyan.baidu.com/album/148a1921f5c5fe4d71c3b105.html?picindex=1"
    proxy_array = [{"http":"127.133.133.133"},{"http":"133.133.133.134"},{"http":"133.133.133.135"},{"http":"133.133.133.136"}]
    for proxy in proxy_array:
        print(proxy)
        try:
            random_proxy =  random.choice(proxy_array)
            with open("linux安装翻墙代理proxychains4.html", "w", encoding="UTF-8")as t:
                t.write(urllib.request.build_opener(urllib.request.ProxyHandler(random_proxy)).open(url).read().decode())
        except Exception as e:
            print(e)


handler_random_proxy()