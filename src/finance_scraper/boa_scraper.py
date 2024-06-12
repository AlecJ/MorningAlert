import os
import time
from typing import List
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from _discord import send_message

class BoAScraper:
    driver: webdriver.Chrome
    timeout = 2

    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.headless = headless
        self.driver = webdriver.Chrome(options=options)

    def quit(self):
        self.driver.quit()

    def login(self):
        self.driver.get("https://www.bankofamerica.com/")
        self.driver.find_element(By.ID, "onlineId1").send_keys(os.environ.get('BOA_USERNAME'))
        self.driver.find_element(By.ID, "passcode1").send_keys(os.environ.get('BOA_PASSWORD'))
        self.driver.find_element(By.ID, "signIn").click()
        time.sleep(self.timeout)

        if self.driver.current_url == "https://secure.bankofamerica.com/login/sign-in/signOnSuccessRedirect.go":
            self.driver.find_element(By.ID, "btnARContinue").click()
            print("input 2fa code: ")
            
            # message user in discord for password
            msg = 'Please enter 2fa code for Bank of America to continue scrape:'
            user_2fa_code = send_message(msg, wait_for_response=True)
            # time.sleep(self.timeout)

            self.driver.find_element(By.CLASS_NAME, "authcode").send_keys()
            self.driver.find_element(By.ID, "yes-recognize").click()
            self.driver.find_element(By.ID, "continue-auth-number").click()
            time.sleep(self.timeout)

    def get_accounts(self) -> List[dict]:
        result = []

        for account in self.driver.find_elements(By.CLASS_NAME, "AccountItem"):
                # print("Found account: {}".format(account.get_name()))
                formatted_account = self.format_account(account)
                result.append(formatted_account)
        
        return result

    def format_account(self, account_element: WebElement) -> dict:
         result = {}

         result['name'] = account_element.find_element(By.TAG_NAME, "a").get_attribute("innerHTML")
         result['url'] = account_element.find_element(By.TAG_NAME, "a").get_attribute("href")

         return result

    def open_account_page(self, account, index=0):
        self.driver.execute_script('window.open()')
        self.driver.switch_to.window(self.driver.window_handles[index + 1])
        self.driver.get(account['url'])
        time.sleep(self.timeout)

    def download_statement(self):
        self.driver.find_element(By.ID, "download-transactions").click()
        Select(self.driver.find_element(By.ID, "select_txnPeriod")).select_by_value("Current transactions")
        Select(self.driver.find_element(By.ID, "select_fileType")).select_by_value("txt")
        self.driver.find_element(By.ID, "btn-download-txn").click()
