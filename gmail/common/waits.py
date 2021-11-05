from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverWaits(object):

    def __init__(self, driver, timeout=10, poll_frequency=1):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)

    def wait_till_alert_is_present(self):
        self.wait.until(EC.alert_is_present(), 'Alert is not present')

    def wait_till_alert_is_dismissed(self):
        self.wait.until(EC.NoAlertPresentException, 'Alert does not get dismissed')

    def wait_till_element_is_present(self, locator):
        self.wait.until(EC.presence_of_element_located(locator), 'Element is not present in the DOM')

    def wait_till_element_is_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator), 'Element is not visible in the DOM')

    def wait_till_element_is_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator), 'Element is not clickable')
