import scrapy

from CnkiSpider1_0.items import LoadSpiderItem


class CnkiSpider(scrapy.Spider):
    # 定义爬虫名字
    name = "daikuan"
    # 定义开始爬取的URL
    start_urls = ['http://daikuan.51kanong.com/daikuan/lists/p/1']

    # 获取index页面内容
    def parse(self, response):

        print(response)
        for info in response.xpath('/html/body/div[1]/div[3]/table/tbody[2]/tr'):
            # 定义存储介质
            item = LoadSpiderItem()
            # print(info.xpath('./td[1]/span/text()').extract())
            item['appName'] = info.xpath('./td[1]/span/text()').extract()
            # //贷款额度
            item['lines'] = info.xpath('./td[2]/text()').extract()
            # 产品描述
            item['describe'] = info.xpath('./td[3]/text()').extract()
            # 费用
            item['cost'] = info.xpath('./td[4]/text()').extract()
            # 申请人数
            item['applications'] = info.xpath('./td[5]/text()').extract()

            yield item

            # 翻页
        for i in range(2,35):
            url = 'http://daikuan.51kanong.com/daikuan/lists/p/'+str(i)
            # print(url)
            yield scrapy.Request(url, self.parse)


