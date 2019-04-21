# -*- coding:utf-8 -*-

from scrapy import cmdline

cmdline.execute('scrapy crawl toScrape'.split())

# cmdline.execute('scrapy crawl toScrape -o toScrape.csv'.split())

# cmdline.execute('scrapy crawl toScrape -o toScrape.json'.split())