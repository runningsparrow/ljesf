# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
#selinum
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#导入 ActionChains 类
from selenium.webdriver import ActionChains
from scrapy.http import HtmlResponse


class LjesfSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        print("process_spider_input===================")
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        print("process_spider_output===================")
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        print("process_start_requests==================")
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        print("spider_opened==================")
        spider.logger.info('Spider opened: %s' % spider.name)


class LjesfDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


#selenium webdriver
#download http://npm.taobao.org/mirrors/chromedriver/
#注明:将chrome浏览器的路径设到环境变量path

class webdriverDownloaderMiddleware(object):
    
    def __init__(self):
        print("init...")
        chromeua = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.68 Safari/537.36"
        dcap = dict(DesiredCapabilities.CHROME)
        dcap["chrome.page.settings.userAgent"] = chromeua
        # self.browser = webdriver.Chrome(executable_path="D:/Down/chromedriver/76.0.3809.68/chromedriver.exe",desired_capabilities=dcap)
        # self.browser = webdriver.Chrome(executable_path="J:/Down1/chromedriver/79.0.3945.36/chromedriver.exe",desired_capabilities=dcap)
        self.browser = webdriver.Chrome(executable_path="J:/Down1/chromedriver/78.0.3904.70/chromedriver.exe",desired_capabilities=dcap)

        super(webdriverDownloaderMiddleware, self).__init__()

    #说明:
    #在类方法里，是无法使用　__init__ 里定义的变量，因为 __init__只在实例化的时候执行，所以需要考虑何种情况下定义类方法
    # @classmethod
    def process_request(self, request, spider):
        print ("start webdriverDownloaderMiddleware process_request")
        print(spider.name)
        # 判断该spider是否为我们的目标
        if spider.name == "esflist":
            self.browser.maximize_window()  # 最大化浏览器窗口
            self.browser.implicitly_wait(2)  # 设置隐式时间等待
            self.browser.get(request.url)

            print (self.browser.title)
            print (self.browser.current_url)

            print("===========================================")
            content = self.browser.page_source
            curl = self.browser.current_url
            print("===========================================")
            # self.browser.close();

            # btnnext = self.browser.find_element_by_xpath('//button[@class="btn-next"]')
            # ActionChains(self.browser).move_to_element(btnnext).click(btnnext).perform()

            
            
            # use find_elements_by_xpath , not find_element_by_xpath
            districtlist = self.browser.find_elements_by_xpath('//div[@data-role="ershoufang"]/div/a')
            print(districtlist)
            districtcount = len(districtlist)
            print(districtcount)

            # if districtcount > 0:
            #     ActionChains(self.browser).move_to_element().click(btnnext).perform()




            print("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{")
            print(self.browser.current_url)
            #将下一页的地址返回给spider
            nexturl = self.browser.current_url
            print("}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
            


            # 直接返回给spider，而非再传给downloader
            # return HtmlResponse(url=curl, body=content, encoding="utf-8", request=request)
            return HtmlResponse(url=nexturl, body=content, encoding="utf-8", request=request)

        else:
            # return None
            pass
        

                   



    def process_response(self, request, response, spider):
        print ("start webdriverDownloaderMiddleware process_response")
        return response


    def process_exception(self, request, exception, spider):
        print ("start webdriverDownloaderMiddleware process_exception")
        print ("error: ")
        print (self.browser)
        print (exception)
        print ("end webdriverDownloaderMiddleware process_exception")