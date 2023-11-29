import scrapy


class TikuSpider(scrapy.Spider):
    name = 'tiku'
    allowed_domains = ['http://www.sdsgwy.com']
    start_urls = ['http://www.sdsgwy.com/article/html/list57-{}.html']
    # 11423
    def start_requests(self):
        for i in range(1, 2):
            yield scrapy.Request(url=self.start_urls[0].format(i), headers={'Cookie': 'UM_distinctid=17c9200427ac41-0ea8331ec6b6ab-b7a1438-144000-17c9200427bc1d; Hm_lvt_8c44646b12108d3e1b2e0c547ecf7b7e=1634537063; ASPSESSIONIDSCBRDQBA=MHMIKCMBKBDJOGLLPGIMKLJC; CNZZDATA1375459=cnzz_eid%3D1246562816-1634527344-https%253A%252F%252Fwww.google.com%252F%26ntime%3D1634527600; Hm_lpvt_8c44646b12108d3e1b2e0c547ecf7b7e=1634538298',
                                           'Host': 'www.sdsgwy.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'})

    def parse(self, response):
        # response.setCharacterEncoding('GB2312')
        print(response.text)
        a = response.xpath('//*[@id="mainlistUL"]/li[2]/span/a/text()')
        print(a)

