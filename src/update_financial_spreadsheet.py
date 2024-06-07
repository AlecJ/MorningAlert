"""
This script runs daily.

It visits Bank of America and USAA's sites to download the latest
banking statements.

It then compiles the data and adds new transactions to a google spreadsheet.
"""

# load env
from dotenv import load_dotenv
load_dotenv()

# load classes
from finance_scraper.boa_scraper import BoAScraper
import time

if __name__ == '__main__':
    boa_scraper = BoAScraper()
    boa_scraper.login()
    time.sleep(5)
    accounts = boa_scraper.get_accounts()
    [print(a) for a in accounts]
    time.sleep(5)
    # driver.quit()