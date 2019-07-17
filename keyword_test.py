from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver=webdriver.Chrome(executable_path="D:/automation/chromedriver")
actions=ActionChains(driver)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id('txtUsername').send_keys("Admin ")
actions.send_keys(Keys.TAB).perform()
time.sleep(3)
driver.get("https://www.myntra.com/")
time.sleep(3)
actions.send_keys(Keys.TAB).perform()
time.sleep(1)
actions.send_keys(Keys.TAB).perform()
time.sleep(1)
actions.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
time.sleep(3)
driver.quit()
