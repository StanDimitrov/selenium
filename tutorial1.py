import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path=PATH)
driver = webdriver.Chrome(service=service, options=options)


web = driver.get("https://www.google.com/")
validate_web = driver.find_element(By.ID, "L2AGLb")
validate_web.click()


driver.find_element(By.NAME, "q").send_keys("roland garros 2022" + Keys.ENTER)

go_ahead = driver.find_element(By.XPATH,'//*[@id="rso"]/div[3]/div/div/div[1]/div/a')
go_ahead.click()
page_validator = driver.find_element(By.ID, 'popin_tc_privacy_button_3').click()
no_mobile_app = driver.find_element(By.ID, 'smart-banner-button-no-thanks').click()