# -*- coding: utf-8 -*-


from scrapy import cmdline

#cmd执行命令
cmd = 'scrapy crawl wdzj '
cmdline.execute(cmd.split())