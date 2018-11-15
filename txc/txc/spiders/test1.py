# -*- coding: utf-8 -*-
import scrapy
import time
import urllib
class Test1Spider(scrapy.Spider):
    name = 'test1'
    firsturl = 'https://www.tianyancha.com/search/suggest.json?'
    allowed_domains = ['https://www.tianyancha.com']
    start_urls = ['https://www.tianyancha.com']
    def start_requests(self):
        data = {"key":"吉昌化学","_":int(time.mktime(time.localtime())*1000)}
        url = Test1Spider.firsturl + urllib.parse.urlencode(data)
        print(url)
        yield scrapy.Request(url=url,callback=self.parse,method="GET")
    def parse(self, response):
        data = response.json()
        print("datajson",data)
    
if __name__ == "__main__":
    print(time.mktime(time.localtime())*1000)
    spider1 = Test1Spider()
    spider1.start_requests()