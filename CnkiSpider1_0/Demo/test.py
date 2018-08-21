#coding=utf-8
import math
import re
import requests
from Cython.Compiler.PyrexTypes import ErrorType
from bs4 import BeautifulSoup
from twisted.python.compat import raw_input
#
# a= 10
# b= 40
# c= 15
#
# temp = b*b-4*a*c
# if temp < 0:
#      raise ErrorType("invalid input")
# a,b,c=float(a),float(b),float(c)
#
#
#
# m = (-b-math.sqrt(temp))/(2*a)
# n = (-b+math.sqrt(temp))/(2*a)
# print(m)
# print(n)
# total = 0
# for i in range (1,11):
#     total = (total + 1000) *( 1 + 0.047)
#
# print(total)
# #!/usr/bin/env python
# #coding: utf-8
# #身体质量指数计算
# weight = float(raw_input())
# high = float(raw_input())
# result = weight/(high ** 2)
# print(result)
# # print '{:.2f}'.format(result)
if __name__ == '__main__':



    # try:
    #     r = requests.get('https://www.p2p001.com/data/index.html',timeout = 30)
    #     # 核心代码
    #     r.raise_for_status()
    #     r.encoding = r.apparent_encoding
    #     print(r.text)
    # except:
    #     print("aaa")


    # url = 'https://www.amazon.cn/dp/B00JZ96ZI8/ref=cngwdyfloorv2_recs_0/462-4833766-6207858?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2&pf_rd_r=Z6NM0S8JGRHHTJ58XJXZ&pf_rd_r=Z6NM0S8JGRHHTJ58XJXZ&pf_rd_t=36701&pf_rd_p=db4e96ef-5fc1-47f8-92b2-b9a5e737b326&pf_rd_p=db4e96ef-5fc1-47f8-92b2-b9a5e737b326&pf_rd_i=desktop'
    # try:
    #     kv = {'user-agent':'Mozilla/5.0'}
    #     r = requests.get(url,headers=kv,timeout = 30)
    #     # 核心代码
    #     print(r.status_code)
    #     r.raise_for_status()
    #     r.encoding = r.apparent_encoding
    #     print(r.text[:1000])
    #     print(r.headers)
    #     r.request
    # except:
    #     print("爬取失败")

    url = 'https://python123.io/ws/demo.html'
    try:
        r = requests.get(url, timeout=30)
        # 核心代码
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        demo = r.text
        soup = BeautifulSoup(demo,"html.parser")
        print(soup.prettify())
        print(soup.title)
        print(soup.a)
        # 标签
        tag = soup.a
        print(tag.attrs)
        # 提取属性中class的值
        print(tag.attrs['class'])
        print(soup.a.parent.name)
        # 获取a标签的字符串
        print(soup.a.string)

        print(soup.head)
        # 子节点
        print(soup.head.contents)

        print(soup.body.contents)
        # print(r.text[:1000])
        # print(r.headers)
        # r.request
        # 上行遍历
        for parent in soup.a.parents:
            if parent is None:
                print(parent)
            else:
                print(parent.name)

        for sibling in soup.a.next_siblings:
            print(sibling)

        for sibling in soup.a.previous_siblings:
            print(sibling)

        print(soup.a.prettify())

        for link in soup.find_all('a'):
            print(link.get('href'))

        for tag in soup.find_all(re.compile('b')):
            print(tag.name)
        print(soup.find_all(id=re.compile('link')))

        print(soup.find_all(string=re.compile("py")))
        print(soup(string=re.compile("py")))
    except:
        print("爬取失败")


