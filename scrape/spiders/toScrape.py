# -*- coding: utf-8 -*-
import scrapy
from scrape.items import ScrapeItem


class ToscrapeSpider(scrapy.Spider):
    name = 'toScrape'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        scrape_list = response.xpath("//div[@class=\"quote\"]")
        for c in scrape_list:
            scrape_item = ScrapeItem()
            scrape_item['text'] = c.xpath(".//span[@class=\"text\"]//text()").extract_first()
            scrape_item['author'] = c.xpath(".//span//small[@class=\"author\"]//text()").extract_first()
            tags = c.xpath(".//div[@class=\"tags\"]//meta//@content").extract_first()
            scrape_item['tags'] = tags.split(",")
            yield scrape_item
        next_link = response.xpath('//nav//ul[@class="pager"]//li[@class="next"]//@href').extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request('http://quotes.toscrape.com/' + next_link, callback=self.parse)
