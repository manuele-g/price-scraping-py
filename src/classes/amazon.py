from datetime import datetime

import constants.constant as const
from classes.product import Product


class Parser(Product):
    """Represents a Amazon Parser."""
    def __init__(self, product):
        self.product_name = product.product_name
        self.url = product.url
        self.limit = product.limit
        self.site = const.AMAZON

    def scrape_price(self, html):
        now = datetime.today().strftime(const.DATE_PATTERN)
        try: 
            price_span = html.find("div", {"id": "rightCol"}).find("div", {"id": "corePrice_feature_div"}).find('span', attrs={'class': 'a-offscreen'})
        except AttributeError:
            price_span = html.find('span', attrs={'class': 'offer-price'})
        price = price_span.text.replace(u'\xa0','')
        second_hand_price = get_used_price(html, self.product_name)
        row = [price, now, self.site]
        data = [row]
        if(second_hand_price is not None):
            data.append([second_hand_price, now, const.AMAZON_SECOND_HAND])
        return data
    
def get_used_price(html, product):
    result = None
    try: 
        used_accordion = html.find("div", {"id": "usedAccordionRow"})
        second_hand_price_span = used_accordion.find("div", {"id": "corePrice_feature_div"}).find('span', attrs={'class': 'a-offscreen'})
        result = second_hand_price_span.text
    except Exception as err:
        try:
            second_hand_price_span = html.find("div", attrs={'class': 'daodi-content'}).find('span', attrs={'class': 'a-offscreen'})
            result = second_hand_price_span.text
        except Exception as err:
            print('Error during scraping second hand price for product ' + product + '. ERROR MESSAGE: ', err)
    return result

