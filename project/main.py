import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'routeur'
    allowed_domains = ['ldlc.com']
    start_urls = ["https://www.ldlc.com/recherche/routeur%204g"]

    def parse(self, response):

        routeur4g = response.css(".listing-product")

        for routeur in routeur4g:
            routeur_name = routeur.css(".listing-product .title-3").get() 
            routeur_rating = routeur.css(".listing-product .ratingClient").get() 
            routeur_picture = routeur.css(".listing-product .pic").get() 
            routeur_price = routeur.css(".listing-product .price").get() 
            routeur_description = routeur.css(".listing-product .price").get() 

            yield{
                    'routeur name':routeur_name,
                    'routeur_rating':routeur_rating,
                    'routeur_picture':routeur_picture,
                    'routeur_price':routeur_price,
                    'routeur_description':routeur_description,
                  }
