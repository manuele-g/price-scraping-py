from classes.product import Product


class ExampleScraper(object):

    def __init__(self):
        self.product_type = 'Example'
        self.products = []
        self.products.append(Product('Example product 1',
                            'https://url1',
                            45))
        self.products.append(Product('Example product 2',
                            'https://url2',
                            35))        

    def execute(self, scraper_factory):
        for product in self.products:
            scraper_factory.get_scraper(product).run(self.product_type)