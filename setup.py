from setuptools import setup

setup(
   name='scrape_fin',
   version='1.0',
   description='A python based scraper for the real estate website REDFIN',
   author='Tanay Shankar',
   author_email='tanaysh7@gmail.com',
   install_requires=['bs4', 'scrapy'], #external packages as dependencies
)