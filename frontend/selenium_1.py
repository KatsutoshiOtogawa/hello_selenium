from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com/?hl=ja")

time.sleep(3000)

driver.quit()