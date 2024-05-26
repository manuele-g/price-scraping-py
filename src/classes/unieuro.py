from datetime import datetime

import constants.constant as const
from classes.product import Product


class Parser(Product):
    """Represents a Unieuro Parser."""
    def __init__(self, product):
        self.product_name = product.product_name
        self.url = product.url
        self.limit = product.limit
        self.site = const.UNIUERO

    def scrape_price(self, html):
        now = datetime.today().strftime(const.DATE_PATTERN)
        price_div = html.find('div', attrs={'class': 'pdp-right__price'})
        integer = price_div.find('span', attrs={'class': 'integer'})
        decimal = price_div.find('span', attrs={'class': 'decimal'})
        currency = price_div.find('span', attrs={'class': 'currency'})
        price = integer.text + decimal.text + currency.text
        price = price.strip()
        return [[price, now, self.site]]