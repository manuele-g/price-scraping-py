from classes.scraper import ScraperFactory
from examplescraper import ExampleScraper

scraper_factory = ScraperFactory()
ExampleScraper().execute(scraper_factory)