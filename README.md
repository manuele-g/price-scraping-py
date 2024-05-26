price-scraping-py: Web Price Scraping for Python
=======================================

What is price-scraping-py?
-------------
It's a library that allows to scrape the product's price on amazon and unieuro and save it the data in a csv file.

Send a telegram notification if the price is less than a threshold.

Send a telegram notification if the second hand price is less than a threshold calculated as COEFF_USED*(new product price). COEFF_USED can be configured in constant.py.

Dependencies (price-scraping-py.toml)
-------------
Dependencies: 
- requests
- beautifulsoup4
- csv
- urllib3[brotli]
- emoji
- pyshorteners

Project Structure 
-------------
The src folder cointans:
- main.py
- classes
    - scraper.py cointains Scraper and ScraperFactory classes. ScraperFactory allows to instantiate the specfic scraper reading the base url. Scraper cointains the algorithm to scrape a price on a web page.
    - product.py cointains a Product class
    - amazon.py cointains the specific scraper for amazon 
    - unieuro.py cointains the specific scraper for amazon
- constants
    - constant.py cointains constants and property values 
- functions
    - notification.py allows to build a message and to send a notification by telegram
    - utility.py cointains utility functions 

How to configure?
-------------

You need:
- to configure the TELEGRAM_CHAT_ID and TELEGRAM_API_KEY propertie in constant.py
- to create python file for each product type you want to scrape as examplescraper.py
- to instantiate the new scraper in main.py


