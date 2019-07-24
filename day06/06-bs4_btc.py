import requests
from bs4 import BeautifulSoup
from lxml import etree
import json

class BtcSpider(object):
    def __init__(self):
        self.base_url = 'https://www.1bd1.com/forum-66-'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
        }
        self.data_list = []
        self.data_detail_list = []
    #1.发请求
    def get_response(self,url):
        response = requests.get(url,headers=self.headers)
        data = response.content.decode('gbk')
        return data

    #2.解析数据list
    def parse_list_data(self,data,rule):
        # html_data = etree.HTML(data)
        # #模糊查询  //tbody[contains(@id,'normalthread')]
        # result_list = html_data.xpath('//tbody[contains(@id,"normalthread")]')
        # result_list = html_data.xpath('//head/following-sibling::*[1]')
        # print(len(result_list))
        # print(result_list)
        soup = BeautifulSoup(data,'lxml')
        #保存列表页的数据
        title_list = soup.select('.xst')
        for title in title_list:
            list_dict_data = {}
            list_dict_data['title'] = title.get_text()
            list_dict_data['detail_url'] =  title.get('href')
            self.data_list.append(list_dict_data)
        return self.data_list

    def parse_detail_data(self,data):
        html_data = BeautifulSoup(data,'lxml')
        #取出问题
        question = html_data.select('#thread_subject')[0].get_text()
        answer_list = html_data.select('.t_f')

        for answer in answer_list:
            answer_list = []
            answer_list.append(answer.get_text())
        detail_data = {
            'question':question,
            'answer':answer_list
        }
        self.data_detail_list.append(detail_data)

    #3.保存数据
    def save_data(self,data,file_path):
        data_str = json.dumps(data)
        with open(file_path, 'w') as f:
            f.write(data_str.replace("\n","").replace("\r",""))

    def start(self):
        self.__init__()
        #列表页的请求
        for i in range(1,3):
            # 1.拼接完整的url
            url = self.base_url + '2.html'
            data = self.get_response(url)
            self.parse_list_data(data,1)
            self.save_data(self.data_list,'06list.json')

        #发送详情页的请求
        for  data in self.data_list:
            detail_url = data['detail_url']
            detail_data = self.get_response(detail_url)
            #解析详情页的数据
            self.parse_detail_data(detail_data)
        self.save_data(self.data_detail_list,'detail.json')
BtcSpider().start()