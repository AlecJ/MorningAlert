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


if __name__ == '__main__':
    # message user

    # poll for response from user

    # print user response




    
    boa_scraper = BoAScraper()
    boa_scraper.login()
    accounts = boa_scraper.get_accounts()

    for i, a in enumerate(accounts):
        boa_scraper.open_account_page(a, i)
        boa_scraper.download_statement()

    boa_scraper.quit()