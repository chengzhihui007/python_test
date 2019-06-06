import requests

url = "http://www.baidu.com"
headers = {"User-Agent":"test"
}

free_proxy = {'http':'121.79.131.58:8080'}

response = requests.get(url=url,headers=headers,proxies=free_proxy)

print(response.status_code)