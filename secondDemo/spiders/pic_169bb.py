# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from secondDemo.items import SeconddemoItem

class Pic169bbSpider(scrapy.Spider):
    name = "pic_169bb"
    allowed_domains = ["169bb.com"]
    start_urls = ['http://169bb.com/']

    def parse(self, response):
        title_list = response.xpath("/html/body/div[@class='header']/div[@class='hd_nav']/div[@class='w1000']//a/text()").extract()
        # print(title_list)
        urldata = response.xpath("/html/body/div[@class='header']/div[@class='hd_nav']/div[@class='w1000']//a/@href").extract()
        #print(urldata)
        xiyang_title = title_list[4] # 获取西洋美女标签的文本内容
        xiyang_urldata = urldata[4]  # 获取西洋美女首页网址
        # print(xiyang_title, xiyang_urldata)
        yield Request(url=xiyang_urldata, callback=self.next)
        # yield Request(url='http://www.169bb.com/xiyangmeinv/2016/0717/36463.html', callback=self.demo)
        # yield Request(url='http://www.169bb.com/xiyangmeinv/2016/0103/2268.html', callback=self.getPic)

    def next(self, response):
        page_num_str = response.xpath("//span[@class='pageinfo']//strong/text()").extract()[0] # 得到西洋美女总页数
        # print(page_num_str)
        # print(response.url)
        for i in range(1, int(page_num_str)+1):
            page_url = response.url + 'list_4_'+ str(i) + '.html' # 得到西洋美女每一个页面的网址
            # print(page_url)
            yield Request(url=page_url, callback=self.next2)
        pass

    def next2(self, response):
        page_title_list = response.xpath("/html/body//div[@class='w1000 box03']/ul[@class='product01']//li/a/@alt").extract()
        # print(page_title_list)
        page_url_list = response.xpath("/html/body//div[@class='w1000 box03']/ul[@class='product01']//li/a/@href").extract()
        # print(page_url_list)

        for i in range(0, len(page_url_list)):
            gril_page_url = page_url_list[i] # 得到西洋美女页面里面每一个美女的网页网址
            print(gril_page_url)
            yield Request(url=gril_page_url, callback=self.next3)
        pass

    def next3(self, response):
        rela_pages_list = response.xpath("//div[@class='dede_pages']/ul//li/a/text()").extract()
        pages_num = len(rela_pages_list) - 3
        # print(pages_num)

        # error
        # self.getPic(response)
        # succes 为啥将下面的代码用self.getPic(response)的形式不能正常的获取到，而使用下面的代码却能获取到？
        item = SeconddemoItem()
        item['url'] = response.xpath("//div[@class='big-pic']/div[@class='big_img']//p/img/@src").extract()
        # print(item['url'])
        # pass
        yield item

        if pages_num == -3:
            # pages_num = 1
            return
        for i in range(2, pages_num+1):
            girl_page_url = response.url.replace('.html', '_') + str(i) + '.html'
            # print(girl_page_url)
            yield Request(url=girl_page_url, callback=self.getPic)
        pass

    def demo(self, response):
    #     rela_pages_list = response.xpath("//div[@class='dede_pages']/ul//li/a/text()").extract()
    #     pages_num = len(rela_pages_list)-3
    #     print(pages_num)
    #     pass
        rela_pages_list = response.xpath("//div[@class='dede_pages']/ul//li/a/text()").extract()
        pages_num = len(rela_pages_list) - 3
        # print(pages_num)

        # error
        # self.getPic(response)
        # succes 为啥将下面的代码用self.getPic(response)的形式不能正常的获取到，而使用下面的代码却能获取到？
        item = SeconddemoItem()
        item['url'] = response.xpath("//div[@class='big-pic']/div[@class='big_img']//p/img/@src").extract()
        # print(item['url'])
        # pass
        yield item

        if pages_num == -3:
            # pages_num = 1
            return
        for i in range(2, pages_num+1):
            girl_page_url = response.url.replace('.html', '_') + str(i) + '.html'
            # print(girl_page_url)
            yield Request(url=girl_page_url, callback=self.getPic)
        pass

    # error : yield 经过了一个中间函数，运行就有问题。我现在还不知道为什么
    # def next4(self, response):
    #     self.getPic(response)
    #     pass

    def getPic(self, response):
        # print(response.url)
        item = SeconddemoItem()
        item['url'] = response.xpath("//div[@class='big-pic']/div[@class='big_img']//p/img/@src").extract()
        # print(item['url'])
        # pass
        yield item




