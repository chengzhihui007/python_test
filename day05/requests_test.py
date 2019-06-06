import requests


url = "https://api.github.com/user"
headers = {"User-Agent":"test1313"}
# auth
auth = ('user', 'pass')
response = requests.get(url, auth=auth,headers=headers)
print(response.status_code)
print(response.headers['content-type'])
print(response.encoding)
print(response.text)
print(response.json())
#proxy
proxy = {'http':'114.113.222.216:80'}
response_proxy = requests.get(url,proxies=proxy)
print(response_proxy.status_code)
print(response_proxy.headers['content-type'])
print(response_proxy.encoding)
print(response_proxy.text)
print(response_proxy.json())
#ssl(verify 默认为True)
requests.packages.urllib3.disable_warnings()
response_ssl = requests.get(url,headers=headers,verify=False)
print(response_ssl.status_code)
print(response_ssl.json())