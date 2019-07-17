from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="D:/automation/chromedriver")
driver.implicitly_wait(8)
actions=ActionChains(driver)

all_url=[]
def youtube_url():
    driver.get("https://www.youtube.com/watch?v=Wb-g7tPO2Gw&list=PLUDwpEzHYYLsMt3L4MnvmsL_DhxUNTW6J&index=1")
    print (driver.title)
    time.sleep(5)
    for i in range(1,3):
        locator=r"(//span[@id='video-title'])[{0}]".format(i)
        print("========================================================================================================================================")
        print("locator======================",locator)
        driver.find_element_by_xpath(locator).click()
        time.sleep(8)
        print("title======================",driver.title)
        print("url======================",driver.current_url)
        all_url.append(driver.current_url)
    driver.quit()

def clipconverter():
    driver.get("https://www.clipconverter.cc/")
    time.sleep(20)
    print("title is===", driver.title)
    handle = driver.current_window_handle
    print("handle====", handle)
    # driver.switch_to.window(handle)
    print("handle====", driver.current_window_handle)
    x=all_url[0]
    print(type(x))
    print(x)
    driver.find_element_by_name("mediaurl").send_keys(x)
    # driver.switch_to.window(handle)
    print("handle====", driver.current_window_handle)
    # driver.find_element_by_xpath("//input[@value='Continue']")
    actions.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
    time.sleep(5)
    # driver.switch_to.window(handle)
    driver.find_element_by_xpath("//input[@value='Start!']").click()
    print("handle====", driver.current_window_handle)
    time.sleep(5)
    url = driver.current_url
    print(url)
    driver.get(url)
    driver.find_element_by_xpath("//strong[text()='Download']").click()
    time.sleep(10)


youtube_url()
print(all_url)
clipconverter()
#
# driver.get("https://www.clipconverter.cc/download/DC62JiJm/423207698/")
# driver.find_element_by_xpath("//strong[text()='Download']").click()
