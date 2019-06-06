import requests

#发送 post

data = {

}
response = requests.post(url, data=data)


#内外 需要 认证
auth = (user,pwd)
response = requests.get(url,auth=auth)
