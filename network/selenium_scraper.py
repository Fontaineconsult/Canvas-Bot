import urllib3
from selenium import webdriver
from dotenv import load_dotenv
import os
from os.path import join, dirname
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



browser_options = webdriver.ChromeOptions()

dotenv_path = join(dirname(__file__), '.env')
chrome_driver_path = join(dirname(__file__), 'chromedriver.exe')
load_dotenv(dotenv_path)
browser_options.headless = True
# browser_options.add_argument("user-data-dir=C:\\Users\\913678186\\AppData\\Local\\Google\\Chrome\\User Data\\Selenium")

prefs = {
    "download_restrictions": 3,  # disable downloads in browser
}
browser_options.add_experimental_option(
    "prefs", prefs
)
browser_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
browser_options.add_argument('log-level=3')

class SeleniumDriver:

    def __init__(self):

        self.driver = webdriver.Chrome(chrome_driver_path, options=browser_options)
        self.driver.set_page_load_timeout(10)
        self.logged_in = False


    def init_duo_session_login(self):

        self.driver.get("https://sfsu.instructure.com/")
        self.driver.get("https://sfsu.instructure.com/login/saml")
        self.driver.find_element(By.XPATH,"//*[@id='username']").send_keys("xxxxxxxxxxxx")
        self.driver.find_element(By.XPATH,"//*[@id='password']").send_keys("xxxxxxxxxxxxxxx")
        self.driver.find_element(By.XPATH,"/html/body/div/div/div/form/div[3]/button").click()
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='duo_iframe']")))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div/form/div[1]/fieldset[1]/div[1]/button"))).click()
        loaded = WebDriverWait(self.driver, 30).until(EC.url_contains("https://sfsu.instructure.com/?login_success=1"))


        if loaded:
            self.logged_in = True
            print("Logged In Successful")


    def init_selenium_canvas_login(self):
        self.driver.get(os.environ.get("canvas_login_site"))
        self.driver.find_element(By.XPATH, "//*[@id='pseudonym_session_unique_id']")\
            .send_keys(os.environ.get("canvas_login_account"))
        self.driver.find_element(By.XPATH, "//*[@id='pseudonym_session_password']")\
            .send_keys(os.environ.get("canvas_login_password"))
        self.driver.find_element(By.XPATH,"//*[@id='login_form']/div[3]/div[2]/button").click()

    def get_page(self, url: str, wait=None, max_timeout=10):
        try:
            self.driver.get(url)
            if wait:
                print(f"waiting {wait} seconds extra for ", url)
                self.driver.implicitly_wait(wait)
                time.sleep(wait + 0.1)
        except TimeoutException:
            print("Stopping Javascript")
            self.driver.execute_script("window.stop();")

        except urllib3.exceptions.ProtocolError as e:
            print(e)

        except urllib3.exceptions.MaxRetryError as e:
            print(e)

        except WebDriverException:
            print("Can't Load Page")
        return self.driver.page_source


    def close_driver(self):
        self.driver.close()


