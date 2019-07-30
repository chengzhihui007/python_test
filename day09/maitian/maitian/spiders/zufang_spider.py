import scrapy

class MaitianSpider(scrapy.Spider):
    name = "zufang"
    start_urls = ["http://bj.5i5j.com/zufang/n1"]

    def parse(self,response):
        # 获取页面中招聘信息在网页中位置节点
        node_list = response.xpath('//div[@class="listCon"]')
        for zufang_item in node_list:
            print(zufang_item)
            areas = zufang_item.xpath('./div[@class="listX"]/p/text()').extract_first()
            area_str = str(areas)
            area = area_str.split('·')[1].replace('平米','').replace(' ','')
            yield {
                'title': zufang_item.xpath('./h3/a/text()').extract_first(),
                'areadetail': zufang_item.xpath('./div[@class="listX"]/p/text()').extract_first(),
                'area': float(area),
                'price': zufang_item.xpath('.//div[@class="jia"]/p/strong/text()').extract_first(),
                'district': zufang_item.xpath('./div[@class="listX"]/p/a/text()').extract_first()
            }

        next_url = response.xpath('//div[@class="pageSty rf"]/a[@class="cPage"]/@href').extract_first()

        if next_url is not None:
            next_page_url = 'http://bj.5i5j.com' +next_url
            yield  scrapy.Request(response.urljoin(next_page_url))
