import scrapy

from ..items import YeTuSpiderItem


class CnkiSpider(scrapy.Spider):
    # 定义爬虫名字
    name = "yetu"
    # 定义开始爬取的URL



    start_urls = ['https://www.yetu.net/product/list-0-0-0---1.html']

    # 定义下一页的列表
    v_nextPageUrl_list = []

    # 获取index页面内容
    def parse(self, response):

        print(response)
        for info in response.xpath('/html/body/div[3]/div/div[1]/div[1]/div/ul/li'):
            # 定义存储介质
            item = YeTuSpiderItem()
            # 存储名称
            item['appName'] = info.xpath("./a/div[1]/div[1]/div[1]/h2/text()").extract()[0]
 
            # 贷款额度
            item['lines'] = info.xpath('./a/div[1]/div[1]/div[2]/span[1]/text()').extract()
            # 借款期限
            item['deadline'] = info.xpath('./a/div[1]/div[1]/div[2]/span[2]/text()').extract()
            # 描述
            item['describe'] = info.xpath('./a/div[1]/div[1]/div[1]/text()').extract()
            # # 费用
            item['dailyRate'] = info.xpath('./a/div[1]/div[2]/span/text()').extract()
            # # 申请人数
            item['advantage'] = info.xpath('./a/div[2]/div/span/text()').extract()
            yield item

        
        

        # # 翻页操作
        for i in range(2,11):
            # https: // www.yetu.net / product / list - 0 - 0 - 0 - --1.html
            url = 'https://www.yetu.net/product/list-0-0-0---'+str(i)+'.html'
            yield scrapy.Request(url, self.parse)





