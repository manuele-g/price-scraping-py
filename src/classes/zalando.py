from datetime import datetime

import constants.constant as const
from classes.product import Product


class Parser(Product):
    """Represents a Zalando Parser."""
    def __init__(self, product):
        self.product_name = product.product_name
        self.url = product.url
        self.limit = product.limit
        self.site = const.ZALANDO

    def scrape_price(self, html):
        now = datetime.today().strftime(const.DATE_PATTERN)
        price_span = html.find("div", attrs={'class': 'hD5J5m'}).find("span", attrs={'class':'sDq_FX'})
        price = price_span.text.replace(u'\xa0','')
        row = [price, now, self.site]
        data = [row]
        return data

