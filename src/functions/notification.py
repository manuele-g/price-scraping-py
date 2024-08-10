import json

import constants.constant as const
import emoji
import pyshorteners
import urllib3


def telegram_notification(message: str):
    headers = {'Content-Type': 'application/json'}
    data_dict = {'chat_id': const.TELEGRAM_CHAT_ID,
                    'text': message,
                    'parse_mode': 'HTML',
                    'disable_notification': False}
    data = json.dumps(data_dict)
    url = f'https://api.telegram.org/bot{const.TELEGRAM_API_KEY}/sendMessage'
    response = urllib3.request("POST",
                    url,
                    headers=headers,
                    body=data)
    return response

def prepare_message(is_used, product_name, price, site, url):
    product_msg = f'{emoji.emojize(':bullseye: ')}{product_name}'
    if is_used:
        used_msg = f'{emoji.emojize(':red_exclamation_mark: ')}PRODOTTO USATO{emoji.emojize(' :red_exclamation_mark:')}'
        product_msg = f'{used_msg}\n{product_msg}'
    site_msg = f'{emoji.emojize(':convenience_store: ')}{site}'
    price_msg = f'{emoji.emojize(':money_bag: ')}{price}'
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(url)
    url_msg = f'{emoji.emojize(':right_arrow: ')}{short_url}'
    return f'{product_msg}\n\n{price_msg}\n{site_msg}\n\n{url_msg}'