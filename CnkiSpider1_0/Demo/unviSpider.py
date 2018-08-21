#coding=utf-8
import math
import re

import bs4
import requests
from Cython.Compiler.PyrexTypes import ErrorType
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""



def fillUnivList(uList,html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        # 过滤非标签
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            uList.append([tds[0].string,tds[1].string,tds[4].string])
    return uList

def printUnivList(uList,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    # 用中文字符填充空格
    print(tplt.format("排名", "学校", "得分",chr(12288)))
    for i in range(0,num):
        u = uList[i]
        print(tplt.format(u[0], u[1], u[2],chr(12288)))


if __name__ == '__main__':
    uinfo = []
    startURL = 'http://www.zuihaodaxue.cn/subject-ranking/computer-science-engineering.html'
    html=getHTMLText(startURL)

    fillUnivList(uinfo,html)

    printUnivList(uinfo,20)


