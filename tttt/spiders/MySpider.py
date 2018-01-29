#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/29 上午10:15
# @Author  : Aries
# @Site    : 
# @File    : MySpider.py
# @Software: PyCharm

import scrapy
from tttt.items import TtttItem

class MySpider(scrapy.Spider):

    name = 'tttt'
    allowed_domains = ["tencent.com"]
    baseURl = "http://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [baseURl + str(offset) ,]

    def parse(self, response):

        node_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')

        for node in node_list :
            item = TtttItem()
            item['positionName'] = node.xpath('./td[1]/a/text()').extract()[0]
            item['positionLink'] = node.xpath("./td[1]/a/@href").extract()[0]

            if len(node.xpath('./td[2]/text()')):
                item['positionType'] = node.xpath("./td[2]/text()").extract()[0]
            else:
                item['positionType'] = ' '

            item['positionCount'] = node.xpath("./td[3]/text()").extract()[0]
            item['positionLoction'] = node.xpath("./td[4]/text()").extract()[0]
            item['positionTime'] = node.xpath("./td[5]/text()").extract()[0]

            yield item

        # if self.offset < 2950 :
        #     self.offset += 10
        #     url = self.baseURl + str(self.offset)
        #     yield scrapy.Request(url, callback=self.parse)
        if not len(response.xpath("//a[@class='noactive' and @id='next']")):
            url = 'http://hr.tencent.com/' + response.xpath("//a[@id='next']/@href").extract()[0]
            yield scrapy.Request(url, callback=self.parse)