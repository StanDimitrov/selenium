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

# Open https://petstore.swagger.io/ (as it is required in our GitHub repository)
web = driver.get("https://petstore.swagger.io/#/")

#select GET method
post_method = driver.find_element(By.CSS_SELECTOR, '#operations-pet-getPetById > div > button.opblock-summary-control > div').click()
params = driver.find_element(By.CLASS_NAME, 'btn try-out__btn')
params.click()

enter_petId = driver.find_element(By.CSS_SELECTOR, '#operations-pet-getPetById > div.no-margin > div > div.opblock-section > div.parameters-container > div > table > tbody > tr > td.parameters-col_description > input[type=text]')
enter_petId.send_keys(1)
validate_button = driver.find_element(By.CLASS_NAME, 'btn execute opblock-control__btn').click()

