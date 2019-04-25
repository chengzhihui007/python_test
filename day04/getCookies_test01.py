import urllib.request


def getCookie_test():
    url = "https://www.yaozh.com/member/";
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Cookie":"acw_tc=2f624a7015561885557473508e5257032d3526adc4ef89bcaefe6943754060; PHPSESSID=lt9afu11hfaq1nc3he3ontqls2; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1556188557; _ga=GA1.2.1527289465.1556188557; _gid=GA1.2.1770025797.1556188557; MEIQIA_VISIT_ID=1KM5KIytKzpUjLs4LpWsGFbXfLW; yaozh_logintime=1556188616; yaozh_user=737659%09chengzhihui007; yaozh_userId=737659; _gat=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1556188617; yaozh_uidhas=1; yaozh_mylogin=1556188621; acw_tc=2f624a7015561885557473508e5257032d3526adc4ef89bcaefe6943754060; MEIQIA_VISIT_ID=1KM5KIytKzpUjLs4LpWsGFbXfLW"}
    request = urllib.request.Request(url,headers=headers)
    handler = urllib.request.HTTPHandler()
    response = urllib.request.build_opener(handler).open(request)
    data =  response.read().decode();
    with open("test.html", "w", encoding="utf-8")as t:
        t.write(data)


getCookie_test()