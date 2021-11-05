import time

from pages.locators import MainNavLocators
from common.waits import DriverWaits


class MainNavigation(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver_waits = DriverWaits(self.driver)

    def logout(self):
        self.driver.find_element(*MainNavLocators.MY_PROFILE_ICON).click()

        self.driver_waits.wait_till_element_is_clickable(MainNavLocators.LOGOUT_LINK)
        time.sleep(1)
        self.driver.find_element(*MainNavLocators.LOGOUT_LINK).click()

        self.driver_waits.wait_till_element_is_visible(MainNavLocators.LOGIN_LINK)
