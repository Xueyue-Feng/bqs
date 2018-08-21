import scrapy


class CnkiSpider(scrapy.Spider):
    # 定义爬虫名字
    name = "kouzi"
    # 定义开始爬取的URL


    i = 322
    start_urls = ['https://www.csai.cn/kouzi/'+str(i)+'.html']

    # 定义下一页的列表
    v_nextPageUrl_list = []

    # 获取index页面内容
    def parse(self, response):
        # 定义字典存储数据
        dic = {}

        # 存储名称
        appName = response.xpath("/html/body/div[3]/div[1]/div[1]/div/div[1]/h1/text()").extract()[0]

        dic.setdefault("名称",appName)
        # 输出名称
        # print(response.xpath("/html/body/div[3]/div[1]/div[1]/div/div[1]/h1/text()").extract())
        # 申请条件
        names=response.xpath("/html/body/div[4]/div/div[2]/ul/li[2]/div[2]/div/span/text()").extract()
        values=response.xpath("/html/body/div[4]/div/div[2]/ul/li[2]/div[2]/div/em/text()").extract()
        # 借款审核细节
        keys2=response.xpath("/html/body/div[4]/div/div[2]/ul/li[3]/div[2]/div/span/text()").extract()
        values2=response.xpath("/html/body/div[4]/div/div[2]/ul/li[3]/div[2]/div/em/text()").extract()
        # print(response.xpath("/html/body/div[4]/div/div[2]/ul/li[3]/div[2]/div/span/text()").extract())
        # print(response.xpath("/html/body/div[4]/div/div[2]/ul/li[3]/div[2]/div/em/text()").extract())
        # 遍历申请条件按字典加入
        for key,value in zip(names,values):
            dic.setdefault(key, value)
        # 遍历借款审核细节按字典加入
        for key,value in zip(keys2,values2):
            dic.setdefault(key, value)
        # print(response.xpath("/html/body/div[4]/div/div[2]/ul/li[2]/div[2]/div/em/text()").extract())
        # 输出最后的结果
        print(dic)
        yield dic
        # 翻页操作
        for i in range(9,321):
            url = 'https://www.csai.cn/kouzi/'+str(i)+'.html'
            # print(url)
            yield scrapy.Request(url, self.parse)





