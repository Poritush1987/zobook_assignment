import settings
from pages.locators import LoginPageLocators
from pages.locators import MainNavLocators
from common.waits import DriverWaits


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver_waits = DriverWaits(self.driver)

    def login(self, credentials=settings.LOGIN_CREDENTIALS):
        self.driver.find_element(*MainNavLocators.LOGIN_LINK).click()
        self.driver_waits.wait_till_element_is_visible(LoginPageLocators.LOGIN_BUTTON)

        email_input = self.driver.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(credentials['email'])

        password_input = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(credentials['password'])

        self.driver_waits.wait_till_element_is_clickable(LoginPageLocators.LOGIN_BUTTON)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        self.driver_waits.wait_till_element_is_visible(MainNavLocators.MY_PROFILE_ICON)
