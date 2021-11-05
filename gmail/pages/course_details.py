from pages.locators import CourseDetailsPageLocators, CheckoutPageLocators
from common.waits import DriverWaits


class CourseDetailsPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver_waits = DriverWaits(self.driver)

    def go_for_enroll(self):
        self.driver.find_element(*CourseDetailsPageLocators.ENROLL_BUTTON_TOP).click()
        self.driver_waits.wait_till_element_is_visible(CheckoutPageLocators.MAIN_BLOCK)
