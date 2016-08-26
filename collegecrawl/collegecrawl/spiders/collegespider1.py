# -*- coding: utf-8 -*-

import scrapy

from collegecrawl.items import CollegecrawlItem

class CollegeSpider(scrapy.Spider):
    name = "colleges"
    allowed_domains = ["colleges.usnews.rankingsandreviews.com"]
    start_urls = [
        'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities'
        #'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities?_page=%s' % page for page in xrange(1,12)
    ]

    #parse the base website national-universities and all the pages
    def parse(self, response):
        for sel in response.xpath('//h3[@class="heading-large block-tighter"]'):
            link = sel.xpath('a/@href').extract()
            #print response.urljoin(link[0])
            yield scrapy.Request(response.urljoin(link[0]), callback=self.parse_summary)

    #school page for us news
    def parse_summary(self, response):
        for par in response.xpath('//div[@class="block-loose"]/p[@class="block-normal"]'):
            #overview = par.xpath('div[@class="block-looser"]/div[@class="clearfix"]/div[@class="block-loose"]/p[@class="block-normal"]/text()')
            overview = par.xpath('text()')
            print overview.extract()
            #summary = par.xpath('div[@id="directoryPageSection-Summary"]/p/text()').extract()
            #print summary
            #now i want to make requests that are outgoing from this page too
        """
        for url in response.css('#side-nav a'):
            newLink = url.xpath('@href').extract()
            link = newLink[0]
            if 'photos' in link:
                pass
            elif 'map' in link:
                pass
            elif 'rankings' in link:
                yield scrapy.Request(response.urljoin(newLink[0]), callback=self.parse_rankings)
            elif 'applying' in link:
                pass
            elif 'academics' in link:
                pass
            elif 'student-life' in link:
                pass
            elif 'campus-safety' in link:
                pass
            elif 'campus-info' in link:
                pass
            elif 'paying' in link:
                yield scrapy.Request(response.urljoin(newLink[0]), callback=self.parse_paying)
        """

    def parse_rankings(self, response):
        print "rankings"

    def parse_paying(self, response):
        print "reached"










    #     for sel in response.xpath('//a[@class="school-name"]'):
    #         item = CollegecrawlItem()
    #         name = sel.xpath('text()').extract()
    #         link = sel.xpath('@href').extract()
    #         print name, link
    #         item['name'] = name
    #         item['link'] = link
    #         item['desc'] = 'N/A'
    #         yield item
#can use //ul/li/a/@href to filter out for links and stuff
