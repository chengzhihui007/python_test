def  http_error():
    #urllib.request 提示错误 HTTPError UrlError
    from urllib import request,error
    url = "http://www.asdfasdf.cn"
    try:
        response = request.urlopen(url)
    except  request.HTTPError as error:
        print(error.code)
    except  error.URLError as errors:
        print(errors)


http_error()
