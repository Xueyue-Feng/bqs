import time

import scrapy
from selenium import webdriver

from CnkiSpider1_0.items import FinancingSpiderItem


class CnkiSpider(scrapy.Spider):
    # 定义爬虫名字
    name = "financing"
    # 定义开始爬取的URL
    start_urls = ['https://shenzhen.rongzi.com/product/']


    # 获取index页面内容
    def parse(self, response):

        print(response)

        driver = webdriver.Firefox()

        driver.get(self.start_urls[0])
        driver.find_element_by_xpath('/html/body/section[3]/div[1]/div/ul[2]/li[3]').click()

        # print('11')
        for j in range(1,16):
            for i in range(1, 11):
                # 定义存储介质
                item = FinancingSpiderItem()
                # 名字
                strXpath = '//section[3]/div[2]/div[' + str(i) + ']/div[1]/div[2]/p[1]/a'
                # print(strXpath)
                print(driver.find_element_by_xpath(strXpath).text)

                item['appName'] = driver.find_element_by_xpath(strXpath).text
                # 利率

                costsXpath = '//section[3]/div[2]/div[' + str(i) + ']/div[2]/div[1]/p[1]/span[2]'
                print(driver.find_element_by_xpath(costsXpath).text)
                if driver.find_element_by_xpath(costsXpath).text:
                    item['lines'] = driver.find_element_by_xpath(costsXpath).text
                else:continue
                # 时间
                timeXpath = '//section[3]/div[2]/div[' + str(i) + ']/div[2]/div[1]/p[2]/span'
                # print(driver.find_element_by_xpath(timeXpath).text)
                if driver.find_element_by_xpath(timeXpath).text:
                    item['cost'] = driver.find_element_by_xpath(timeXpath).text
                else:continue
                # # 条件
                # conditionsXpath = '//section[3]/div[2]/div[' + str(i) + ']/div[1]/div[2]/p[2]'
                # print(driver.find_element_by_xpath(conditionsXpath).text)
                # # 要求
                # requirementsXpath = '//section[3]/div[2]/div[' + str(i) + ']/div[1]/div[2]/div/p/a'
                # print(driver.find_element_by_xpath(requirementsXpath).text)
                yield item
            time.sleep(1)
            if j < 4:
                driver.find_element_by_xpath('/html/body/section[3]/div[3]/div/ul/li[8]').click()
            else:
                driver.find_element_by_xpath('/html/body/section[3]/div[3]/div/ul/li[9]').click()



