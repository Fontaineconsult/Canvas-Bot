import time

import requests
from colorama import Fore, Style
from requests.exceptions import ConnectionError, ReadTimeout, TooManyRedirects

from network.selenium_scraper import SeleniumDriver
import urllib3
from config.read import read_config
requests_settings = read_config()['requests']
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


from fake_useragent import UserAgent
ua = UserAgent()
print(ua.chrome)



class CanvasSession:

    def __init__(self):
        self.RequestsSession = requests.session()
        self.SeleniumSession = SeleniumDriver()
        self.selenium_cookies = None
        self.max_retries = 1

    def _init_selenium_login(self):
        print("Logging in with Selenium")
        self.SeleniumSession.init_selenium_canvas_login()
        self.selenium_cookies = self.SeleniumSession.driver.get_cookies()

    def _init_requests_session(self):
        print("Setting requests cookies")
        for cookie in self.selenium_cookies:
            self.RequestsSession.cookies.set(domain=cookie['domain'],
                                             name=cookie['name'],
                                             value=cookie['value'])

    def init(self):
        self._init_selenium_login()
        self._init_requests_session()

    def requests_get(self, url):
        headers = requests_settings['user-agent']
        print("Requests get", url)
        try:
            request = self.RequestsSession.get(url, verify=False, headers=headers, timeout=10)
            if not request.ok:
                print(f"{Fore.LIGHTRED_EX}Request Received Code: {request.status_code} {url}{Style.RESET_ALL}")
                if request.status_code == 400:
                    print(request.content, request.headers)
                return None
            return request

        except ConnectionError:
            print(f"{Fore.LIGHTRED_EX}Connection Error {url}{Style.RESET_ALL}")
            return None
        except ReadTimeout:
            print(f"{Fore.LIGHTRED_EX}Connection Timed Out {url}{Style.RESET_ALL}")
            return None
        except TooManyRedirects:
            print(f"{Fore.LIGHTRED_EX}Too Many Redirects {url}{Style.RESET_ALL}")
            return None

    def requests_header(self, url):
        return self.RequestsSession.head(url, verify=True)

    def selenium_get(self, url, wait=None, retry_count=0):
        print("Selenium get", url)
        try:
            if wait:
                return self.SeleniumSession.get_page(url, wait)
            else:
                return self.SeleniumSession.get_page(url)
        except urllib3.exceptions.MaxRetryError as e:
            if retry_count < self.max_retries:
                time.sleep(2)
                print(f"Max Retry Error: retrying {retry_count + 1} site:", url)
                self.selenium_get(url, retry_count=retry_count+1)
            else:
                print(e)
                return None
