import csv
import time

import constants.constant as const
import requests
from bs4 import BeautifulSoup
from functions.notification import prepare_message, telegram_notification
from functions.utility import extract_numbers


class Scraper(object):
    def __init__(self, parser, url):
        self._parser = parser
        self.url = url

    def _download(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        response = requests.get(self.url, headers = headers)
        html = BeautifulSoup(response.content, 'html.parser')
        return html

    def _store(self, data, path):
        print(data)
        existing_rows = []
        try:
            with open(path, 'r',newline='', encoding=const.UTF8_ENCODING) as readFile:
                rd = csv.reader(readFile)
                existing_rows = [line for line in rd]
        except FileNotFoundError:
            print('...Creating file: ', path)
        with open(path, mode='w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(data)
                writer.writerows(existing_rows)

        if 'readFile' in locals():
            readFile.close()
        csvfile.close()
   
    def _send_notification(self, price, second_hand_price):

        try:
            float_price = extract_numbers(price)
            float_second_hand_price = extract_numbers(second_hand_price)
            if(float_price <= self._parser.limit):
                message = prepare_message(False, self._parser.product_name, price, self._parser.site, self._parser.url)
            if(float_second_hand_price < float_price*const.COEFF_USED):
                message = prepare_message(True, self._parser.product_name, second_hand_price, self._parser.site, self._parser.url)
            if 'message' in locals():
                telegram_notification(message)
        except Exception as err:
            print(err)

    def run(self, product_type):
        try:
            html = self._download()
            parser = self._parser
            print(parser.product_name)
            data = parser.scrape_price(html)
            path = const.FOLDER +  product_type + '_' + parser.product_name + '.csv'
            self._store(data, path)
            length = len(data)
            price = data[0][0]
            second_hand_price = data[1][0] if length > 1 else price
            self._send_notification(price, second_hand_price)
            time.sleep(2)
        except Exception as err:
            print(err)
            print('Error during scraping for product ' + parser.product_name + '. ERROR MESSAGE: ', err)

class ScraperFactory:
    def get_scraper(self, product):
            if(const.AMAZON.lower() in product.url):
                product_class = __import__('classes.amazon', fromlist=['object'])
            elif (const.UNIUERO.lower() in product.url):
                product_class = __import__('classes.unieuro', fromlist=['object'])
            elif (const.ZALANDO.lower() in product.url):
                product_class = __import__('classes.zalando', fromlist=['object'])
            parser = product_class.Parser(product)
            return Scraper(parser, product.url)