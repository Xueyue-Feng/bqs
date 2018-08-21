
import scrapy





class CnkiSpider(scrapy.Spider):
    # 定义爬虫名字
    name = "dailuopan"
    # 定义开始爬取的URL
    start_urls = ['http://www.dailuopan.com/data']
    # 获取index页面内容
    def parse(self, response):
        # 定义字典存储数据
        print(response)
        for i in range(1,304):
            s1 =  response.xpath("/html/body/div[2]/div[2]/div/div[3]/div/table/tbody/tr[" + str(i) + "]/td[2]/a/text()").extract()[0]
            s2 = response.xpath("/html/body/div[2]/div[2]/div/div[3]/div/table/tbody/tr["+str(i)+"]/td[3]/text()").extract()[0]
            s3 = response.xpath("/html/body/div[2]/div[2]/div/div[3]/div/table/tbody/tr["+str(i)+"]/td[4]/text()").extract()[0]
            s4=response.xpath("/html/body/div[2]/div[2]/div/div[3]/div/table/tbody/tr["+str(i)+"]/td[5]/text()").extract()[0]
            s5=response.xpath("/html/body/div[2]/div[2]/div/div[3]/div/table/tbody/tr["+str(i)+"]/td[6]/text()").extract()[0]
            s6=response.xpath("/html/body/div[2]/div[2]/div/div[3]/div/table/tbody/tr["+str(i)+"]/td[7]/text()").extract()[0]
            s7=response.xpath("/html/body/div[2]/div[2]/div/div[3]/div/table/tbody/tr["+str(i)+"]/td[8]/text()").extract()[0]
            s8=response.xpath("/html/body/div[2]/div[2]/div/div[3]/div/table/tbody/tr["+str(i)+"]/td[9]/text()").extract()[0]
            print(s1 +"\t"+ s2 +"\t"+ s3 +"\t"+s4+"\t"+s5+"\t"+s6+"\t"+s7+"\t"+s8)







