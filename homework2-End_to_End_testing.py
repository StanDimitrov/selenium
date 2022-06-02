import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys

# PATH Configuration
PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path=PATH)
driver = webdriver.Chrome(service=service, options=options)

# Open google and search for 'Alphabet share price'. (as it is required in our GitHub repository)
web = driver.get("https://www.google.com/")
validate_web = driver.find_element(By.ID, "L2AGLb")
validate_web.click()

# Check to see if the search results are showing up
driver.find_element(By.NAME, "q").send_keys("Alphabet share price" + Keys.ENTER)

# Go to yahoo finance link and confirm the page loads
confirmation_page = driver.find_element(By.XPATH, "//a[@href='https://finance.yahoo.com/quote/GOOG/']")
confirmation_page.click()

# Validation the page
validat_cookies = driver.find_element(By.XPATH, '//*[@id="consent-page"]/div/div/div/form/div[2]/div[2]/button[1]').click()
