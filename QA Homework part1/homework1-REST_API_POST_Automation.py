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

#select POST method
post_method = driver.find_element(By.CLASS_NAME, 'opblock-summary-description').click()

#Try it out button
button_avtivation = driver.find_element(By.CLASS_NAME, 'btn try-out__btn').click()

#Enter pet characters
enter_pet_id = driver.find_element(By.CSS_SELECTOR, "#operations-pet-uploadFile > div.no-margin > div > div.opblock-section > div.parameters-container > div > table > tbody > tr:nth-child(1) > td.parameters-col_description > input[type=text]").send_keys("1" + Keys.ENTER)
enter_additional_data = driver.find_element(By.CSS_SELECTOR, '#operations-pet-uploadFile > div.no-margin > div > div.opblock-section > div.parameters-container > div > table > tbody > tr:nth-child(2) > td.parameters-col_description > input[type=text]').send_keys('{"bread" : "chihjuahua", "name" : "Sparky", "age": "1"}' + Keys.ENTER)
upload_photo = driver.find_element(By.XPATH, '#operations-pet-uploadFile > div.no-margin > div > div.opblock-section > div.parameters-container > div > table > tbody > tr:nth-child(3) > td.parameters-col_description > input[type=file]').send_keys('C://Users/Stan/Desktop/esperance-vie-chihuahua.jpg')







