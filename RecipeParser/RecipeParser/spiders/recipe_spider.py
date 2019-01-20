import scrapy
import parser


class RecipeScraper(scrapy.Spider):
    name = "recipes"

    #def start_requests(self):
    start_urls = [
        'http://www.seriouseats.com/recipes/2009/12/perfect-prime-rib-beef-recipe.html',
    ]
    #    for url in urls:
    #        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        NewSeriousEatsRecipe = parser.Recipe()