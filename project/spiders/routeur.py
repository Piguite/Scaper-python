import scrapy

def get_brand(response):
    features = response.css('[id="product-parameters"] tr td')
    for i, line in enumerate(features):
        if "Marque" in line.css('::text').get():
            return features[i + 1].css('label ::text').get()


class SpiderSpider(scrapy.Spider):
    name = 'routeur'
    domain = 'https://www.ldlc.com'
    allowed_domains = ['ldlc.com', ]


    def start_requests(self):
        urls = [
            'https://www.ldlc.com/recherche/routeur%204g/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
         for link in response.css('.pdt-item .title-3 ::attr(href)'):
            yield scrapy.Request(url=f'{self.domain}{link.get()}', callback=self.parse_detail_products, dont_filter=True)

    def parse_detail_products(self,response):

        yield {
            'name': response.css('.product-bloc h1::text').get().strip(),
            'brand': get_brand(response),
            'price': response.css('div.price::text').get() +
                     response.css('div.price sup::text').get(),
            'desc': response.css('.product-bloc h2::text').get().replace('\n',''),
            'image': response.css('.desc-image img ::attr(src)').get(),
            "note": response.css(".sbloc.details-pdt .note ::text").get()
        }