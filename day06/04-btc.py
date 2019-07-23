import requests
from lxml import  etree
import  json

class BtcSpider(object):
    def _init_(self):
        self.base_url = 'https://www.1bd1.com/forum-66-'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
        }

# 1.发请求
    def get_response(self,url):
        responses = requests.get(url,headers=self.headers)
        data = responses.content.decode('gbk')
        return data

# 2.解析数据
    def parse_data(self,data):
        #使用xpath 解析当前页面 所有的 新闻title 和url 保存
        # 1.转型
        x_data = etree.HTML(data)
        # 2.根据xpath路径解析
        title_list = x_data.xpath('//a[@class="s xst"]/text()')
        url_list = x_data.xpath('//a[@class="s xst"]/@href')

        data_list = []
        for index,title in enumerate(title_list):
            news = {}
            news['name'] = title
            news['url'] = url_list[index]
            data_list.append(news)
        return data_list

# 3.保存数据
    def save_data(self,data):
        #将list--str
        data_str = json.dumps(data)
        with open('05btc.json', 'w', encoding='gbk') as f:
            f.write(data_str)
# 4. 启动
    def run(self):
        self._init_()
        # 1.拼接完整的url
        url = self.base_url + '2.html'
        # 2.发请求
        data = self.get_response(url)
        # 3.做解析
        parse_data = self.parse_data(data)
        # 4.保存
        self.save_data(parse_data)





BtcSpider().run()
