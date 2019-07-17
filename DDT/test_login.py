import time
import Xutils
from selenium import webdriver
driver=webdriver.Chrome(executable_path="D:/automation/chromedriver")
driver.get("http://newtours.demoaut.com/")
path="D:\sel_py_training\DDT\data.xlsx"
rows=Xutils.getRowsCount(path,"Sheet1")
columns=Xutils.getColumnsCount(path,"Sheet1")
print(rows)
print(columns)

def test_loginCheck():
    for r in range(2,rows+1):
        username=Xutils.readData(path,"Sheet1",r,1)
        password=Xutils.readData(path, "Sheet1", r, 2)
        driver.find_element_by_name("userName").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        Xutils.logger.info("logging..................")
        driver.find_element_by_name("login").click()
        if driver.title == "Find a Flight: Mercury Tours:":
            Xutils.logger.info("logged successfully")
            print("Passed.............")
            Xutils.writeData(path,"Sheet1",r,3,"passed")

        else:
            driver.save_screenshot("login_fail.jpg")
            #driver.get_screenshot_as_file("login_fail.png")
            Xutils.logger.info("logging failed")
            print("failed........")
            Xutils.writeData(path, "Sheet1", r, 3, "failed")
        time.sleep(3)
        driver.find_element_by_link_text("Home").click()
test_loginCheck()
time.sleep(3)
driver.quit()