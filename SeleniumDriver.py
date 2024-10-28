from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumDriver:
    def __init__(self, browser="chrome", timeout=10):
        if browser == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser == "firefox":
            from webdriver_manager.firefox import GeckoDriverManager
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            raise ValueError("Browser not supported!")
        self.driver.implicitly_wait(timeout)

    def open_url(self, url):
        """Opens a URL in the browser"""
        self.driver.get(url)

    def get_title(self):
        """Returns the title of the current page"""
        return self.driver.title

    def get_element(self, locator, locator_type=By.ID):
        """Finds a web element on the page"""
        return self.driver.find_element(locator_type, locator)

    def get_elements(self, locator, locator_type=By.ID):
        """Finds multiple web elements on the page"""
        return self.driver.find_elements(locator_type, locator)

    def click_element(self, locator, locator_type=By.ID):
        """Clicks on a web element"""
        element = self.get_element(locator, locator_type)
        element.click()

    def send_keys(self, locator, text, locator_type=By.ID):
        """Sends text to a web element"""
        element = self.get_element(locator, locator_type)
        element.send_keys(text)

    def get_text(self, locator, locator_type=By.ID):
        """Gets text from a web element"""
        element = self.get_element(locator, locator_type)
        return element.text

    def select_dropdown_by_value(self, locator, value, locator_type=By.ID):
        """Selects a dropdown option by value"""
        element = self.get_element(locator, locator_type)
        select = Select(element)
        select.select_by_value(value)

    def select_dropdown_by_visible_text(self, locator, text, locator_type=By.ID):
        """Selects a dropdown option by visible text"""
        element = self.get_element(locator, locator_type)
        select = Select(element)
        select.select_by_visible_text(text)

    def hover_over_element(self, locator, locator_type=By.ID):
        """Hovers over a web element"""
        element = self.get_element(locator, locator_type)
        ActionChains(self.driver).move_to_element(element).perform()

    def wait_for_element(self, locator, locator_type=By.ID, timeout=10):
        """Waits for a web element to be present on the page"""
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((locator_type, locator))
        )

    def is_element_visible(self, locator, locator_type=By.ID, timeout=10):
        """Checks if a web element is visible on the page"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((locator_type, locator))
            )
            return True
        except:
            return False

    def switch_to_frame(self, locator, locator_type=By.ID):
        """Switches to an iframe"""
        element = self.get_element(locator, locator_type)
        self.driver.switch_to.frame(element)

    def switch_to_default_content(self):
        """Switches back to the default content from iframe"""
        self.driver.switch_to.default_content()

    def accept_alert(self):
        """Accepts an alert"""
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        """Dismisses an alert"""
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def quit_driver(self):
        """Quits the WebDriver session"""
        self.driver.quit()
