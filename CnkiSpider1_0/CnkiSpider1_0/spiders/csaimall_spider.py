import scrapy


class CnkiSpider(scrapy.Spider):
    # 定义爬虫名字
    name = "csaimall"
    # 定义开始爬取的URL
    start_urls = ['https://daikuan.csaimall.com/product-13001.html']
    # 获取index页面内容
    def parse(self, response):
        # 定义字典存储数据
        print(response)
        dic = {}
        # 名称
        贷款名称=response.xpath("/html/body/div[5]/div[2]/div[1]/div[1]/div[3]/dl/dt/strong[1]/text()").extract()
        dic.setdefault('贷款名称', 贷款名称)
        # print(response.xpath("/html/body/div[5]/div[2]/div[1]/div[1]/div[3]/dl/dt/strong[1]/text()").extract())
        # 公司
        公司=response.xpath("/html/body/div[5]/div[2]/div[1]/div[1]/div[3]/dl/dt/strong[2]/a/text()").extract()
        dic.setdefault('公司', 公司)
        # print(response.xpath("/html/body/div[5]/div[2]/div[1]/div[1]/div[3]/dl/dt/strong[2]/a/text()").extract())
        # print(response.xpath('/html/body/div[5]/div[2]/div[1]/div[1]/dl/dd/p//text()').extract())
        # 存放数据的数组
        # ['\r\n                                ', '贷款金额：', '0.1-5万', '\r\n                                ', '月利率：',
        #  '0.55-1.99%', '\r\n                            ', '\r\n                                ', '贷款期限：',
        #  '不限-24\r\n个月\t\t\r\n                            ', '\r\n                                ', '月管理费率：', '0-0%',
        #  '\r\n                            ', '\r\n                                ', '放款时间：',
        #  '1个工作日\r\n                            ', '\r\n                                ', '手续费率：', '3-3%',
        #  '\r\n\t\t\t\t\t\t\t']
        dataArray=response.xpath('/html/body/div[5]/div[2]/div[1]/div[1]/dl/dd/p//text()').extract()

        # 贷款金额
        贷款金额 = dataArray[2]
        dic.setdefault('贷款金额', 贷款金额)
        # print(dataArray[2])
        # 月利率
        月利率 = dataArray[5]
        dic.setdefault('月利率', 月利率)
        # print(dataArray[5])
        # 贷款期限
        贷款期限 = dataArray[9].strip().replace("\r","").replace("\n","").replace("\t","")
        dic.setdefault('贷款期限', 贷款期限)
        # print(dataArray[9].replace("\r","").replace("\n","").replace("\t",""))
        # 月管理费率
        月管理费率 = dataArray[12]
        dic.setdefault('月管理费率', 月管理费率)
        # print(dataArray[12])
        # 放款时间
        放款时间 = dataArray[16].strip()
        dic.setdefault('放款时间', 放款时间)
        # print(dataArray[16].strip())
        # 手续费率
        手续费率 = dataArray[19]
        dic.setdefault('手续费率', 手续费率)
        # print(dataArray[19])
        yield dic

        # 翻页操作
        for i in range(13002,14000,1):
            url = 'https://daikuan.csaimall.com/product-'+str(i)+'.html'
            # print(url)
            yield scrapy.Request(url, self.parse)





