from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.seleniumeasy.com/selenium-webdriver-tutorials')

searchField = driver.find_element(By.XPATH, '/html/body/header/div/div[1]/div/section/form/div/div/div[1]/input')
print(searchField)
searchField.send_keys('Navigating')
searchButton = driver.find_element(By.XPATH, '/html/body/header/div/div[1]/div/section/form/div/div/div[1]/span/button/span')
searchButton.click()
