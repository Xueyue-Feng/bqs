import scrapy

from ..items import YeTuSpiderItem, wdzjSpiderItem


class CnkiSpider(scrapy.Spider):
    # 定义爬虫名字
    name = "wdzj"
    # 定义开始爬取的URL
    start_urls = ['https://www.wdzj.com/dangan/search?filter=e1&currentPage=1']

    # 获取index页面内容
    def parse(self, response):
        print(response)

        for info in response.xpath('/html/body/div[4]/div[2]/div[3]/div[2]/ul/li'):
            #     # 定义存储介质
            item = wdzjSpiderItem()
            # 存储名称
            item['appName'] = info.xpath("./div[1]/h2/a/text()").extract()[0]
            # 上线时间
            timeOnline = info.xpath('./div[2]/a/div[4]/text()').extract()[0].split('：')[1]
            item['timeOnline'] = timeOnline
            # # 费用
            item['rate'] = info.xpath('./div[2]/a/div[1]/label/em/text()').extract()
            # # 申请人数
            item['score'] = info.xpath('./div[2]/a/div[5]/strong/text()').extract()
            yield item

        # # 翻页操作
        for i in range(2,67):
            # https: // www.yetu.net / product / list - 0 - 0 - 0 - --1.html
            url = 'https://www.wdzj.com/dangan/search?filter=e1&currentPage='+str(i)
            yield scrapy.Request(url, self.parse)
