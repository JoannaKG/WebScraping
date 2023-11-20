from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
for i in range(1, 8):
    sourceXPath = '//*[@id="box{}"]'.format(i)
    destinationXPath = '//*[@id="box10{}"]'.format(i)
    source = driver.find_element(By.XPATH, sourceXPath)
    destination = driver.find_element(By.XPATH, destinationXPath)
    actions = ActionChains(driver)
    actions.drag_and_drop(source, destination).perform()


