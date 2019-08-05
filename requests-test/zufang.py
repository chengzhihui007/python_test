import datetime
import random
from multiprocessing.pool import ThreadPool
from time import sleep

import  requests
import execjs
from bs4 import  BeautifulSoup
from selenium import webdriver
import re
#Pool线程池
from multiprocessing.dummy import Pool as Threadpool
import json
from pymongo import MongoClient
class ZufangSpider():

    def __init__(self):
        option = webdriver.ChromeOptions()
        # option.add_argument('headless')
        self.driver = webdriver.Chrome(
        executable_path='H:/workspace/软件/chromedriver_win32/chromedriver',
        chrome_options=option
        )
        self.base_url = 'https://bj.5i5j.com'
        self.start_url = '/zufang'
        self.my_headers = [
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
        ]
        header = random.choice(self.my_headers)
        self.headers = {'User-Agent': header}
        self.count = 0
        # 收集到的常用Header
        self.area_url_list = []

    def get_area_url(self,url):
         self.driver.get(url)
         self.bs4_data(self.driver.page_source)

    def get_area_data(self,url):
        print("xxx")
        self.driver.get(url)
        self.bs4_area_data(self.driver.page_source)

    def bs4_area_data(self,data):
        bs4_data = BeautifulSoup(self.driver.page_source, 'lxml')

        next_url = bs4_data.select_one('.cPage')
        if next_url is None:
            return
        next_href = next_url.get('href')
        self.count = self.count+1
        if self.count ==  3:
            self.count = 0
            return
        if(next_href is not None):
            url = self.base_url+next_href
            print(url)
            self.get_area_data(url)

    def bs4_data(self,data):
        bs4_data = BeautifulSoup(self.driver.page_source, 'lxml')
        area_list = bs4_data.select('.new_di_tab')[0].select('a')

        for area in area_list:
            area_url = area.get('href')
            if  area_url.count("/") == 3 :
                url = self.base_url+area_url
                print(url)
                self.area_url_list.append(url)






    def start(self):
     self.get_area_url(self.base_url+self.start_url)
     for area_url in self.area_url_list :
        self.get_area_data(area_url)
        print(area_url)
     # pool = ThreadPool(4)
     # pool.map(self.get_area_data,self.area_url_list)
     # pool.close()
     # pool.join()


ZufangSpider().start()