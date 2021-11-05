import settings
from pages.locators import HomePageLocators
from common.waits import DriverWaits


class HomePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver_waits = DriverWaits(self.driver)

    def load_home_page(self):
        self.driver.get(settings.BASE_URL)