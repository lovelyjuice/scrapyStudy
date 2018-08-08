import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from scrapyStudy.items import ScrapystudyItem


class MySpider(scrapy.Spider):
    name = 'scrapyStudy'
    allowed_domains = ['23wx.cc']
    bash_url = 'http://www.23wx.cc/class/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1, 11):
            url = self.bash_url + str(i) + '_1' + self.bashurl
            yield Request(url, self.parse)
        yield Request('http://www.23wx.cc/quanben/1', self.parse)

    def parse(self, response):
        yield Request(response.url, self.get_name)

    def get_name(self, response):
        lis = BeautifulSoup(response.text, 'lxml').select('div.l ul li')
        for li in lis:
            novelName = li.select_one('.s2 a').text
            novelUrl = li.select_one('.s3 a')['href']
            yield Request(novelUrl, self.get_chapter_url, meta={'name': novelName, 'url': novelUrl})

    def get_chapter_url(self,response):
        item=ScrapystudyItem()
        item['name']=str(response.meta['name']).strip()
        item['novelUrl']=str(response.meta['novelUrl']).strip()
        page=BeautifulSoup(response.text,'lxml')
        item['author']=page.select_one('#info > p:nth-of-type(1)').text.partition('：')[-1]
        item['lastUpdate']=page.select_one('#info > p:nth-of-type(4)').text.partition('：')[-1]
        item['description']=page.select_one('#intro p').text.strip()
        item['nameId']=response.url[-6:-1]
        return item


