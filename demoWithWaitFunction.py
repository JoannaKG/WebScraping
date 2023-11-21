from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

url = 'https://earth.google.com/web/'
driver.get(url)

wait = WebDriverWait(driver, 20)
searchField = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/flutter-view/flt-text-editing-host/form/input[2]')))
searchField.send_keys('Warsaw\n')

