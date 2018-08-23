# -*- coding: utf-8 -*-

from scrapy import Request
from scrapy.spiders import Spider
from github_rank.items import GithubRankItem
from github_rank.tran_cookie import transCookie

class GithubRankSpider(Spider):
    name = 'github_rank_top'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    url_pre = 'https://github.com/search?l=' 
    lang = 'JavaScript'
    url_pre1= '&o=desc&p=' 
    url_suf = '&q=stars%3A%3E1&s=stars&type=Repositories'
    # pages = 1 

    def __init__(self, lang="JavaScript"):
        self.lang = lang 
        # self.pages = pages

    def start_requests(self):
        # 使用 cookie 避免429 
        cookies = transCookie.stringToDict() 
        url = self.url_pre + self.lang + self.url_pre1 + str(1) + self.url_suf 
        yield Request(url, headers=self.headers, cookies=cookies)

    def parse(self, response):
        # response 
        # <200 https://github.com/search?l=JavaScript&o=desc&p=1&q=stars%3A%3E1&s=stars&type=Repositories>
        # print response.body 

        item = GithubRankItem()
        ## 找到list
        # repos = response.xpath('//ol[@class="grid_view"]/li')
        # repos = response.xpath('//ul[@class="repo-list"]/li')

        # repos = response.xpath('//h3/a[@class="v-align-middle"]')

        # repos = response.xpath('//div[@class="col-12 col-md-8 pr-md-3"]')

        repos = response.xpath('//div[@class="repo-list-item d-flex flex-column flex-md-row flex-justify-start py-4 public source"]')
        print repos 

        for repo in repos:
            
            # item['repo'] = repo.xpath(
            #     './/div[@class="hd"]/a/span[1]/text()').extract()[0]

            item['repo'] = repo.xpath(
                # './/div[0]/h3/a/text()').extract()    
                # './/h3/a/text()').extract()[0]
                './/div[@class="col-12 col-md-8 pr-md-3"]/h3/a/text()').extract()[0]

            item['sub_title'] = ("".join(repo.xpath(
                # './/div[0]/p[@class="col-12 col-md-9 d-inline-block text-gray mb-2 pr-4"]/text()'
                # './/p[@class="col-12 col-md-9 d-inline-block text-gray mb-2 pr-4"]/text()'
                './/div[@class="col-12 col-md-8 pr-md-3"]/p[@class="col-12 col-md-9 d-inline-block text-gray mb-2 pr-4"]/text()'
            ).extract())).replace("\n","").strip(" ")

            item['rank'] = ("".join(repo.xpath(
                './/div[@class="flex-shrink-0 col-6 col-md-4 pt-2 pr-md-3 d-flex"]/div[@class="pl-2 pl-md-0 text-right flex-auto min-width-0"]/a/text()'
                ).extract())).replace("\n","").strip(" ")

            # item['link'] = repo.xpath(
            #     './/div[@class="star"]/span/text()').re(ur'(\d+)人评价')[0]
            item['link'] = "https://github.com/" + item['repo'] 
            yield item

        i = 2 
        while i <= 11 :
            next_url = self.url_pre + self.lang + self.url_pre1 + str(i) + self.url_suf 
            yield Request(next_url, headers=self.headers)
            i += 1 