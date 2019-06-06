import requests

headers = {"User-Agent":"test"}

#session类 可以自动保存cookie
session = requests.session()
#1 代码登陆
login_url = "https://www.yaozh.com/login"
member_url = "https://www.yaozh.com/member"
login_form_data = {
    "a":"testa",
    "b":"testb",
    "c":"testc"
}

#登陆成功，自动保存cookies
login_responses = session.post(login_url,data=login_form_data)

#2.登陆成功之后 带着 有效的cookies 访问 请求目标数据
data = session.get(member_url,headers=headers).content.decode()
