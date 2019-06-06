import requests

#请求数据URL
member_url = "https://www.yaozh.com/member"

headers = {
    "User-Agent":"test"
}
#cookies的字符串
cookies = "sdsdfafa=aaaaaa;aaaaa=bbbbbb"

cook_dict = {}

cookies_list = cookies.split(";")

cook_dict = {cookie.split("=")[0]:cookie.split("=")[1] for cookie in cookies_list}
print(cook_dict)

c = { s for s in {10,11}}
print(c)


#需要的是cookie的字典类型
