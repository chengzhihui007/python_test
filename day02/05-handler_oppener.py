import  urllib.request


def handler_oppener():
    url = "https://blog.csdn.net/anonymous_qsh/article/details/79349068"
    handler = urllib.request.HTTPHandler()
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    with open("handler_oppener.html", "w", encoding="UTF-8")as t:
        t.write(response.read().decode())


handler_oppener()