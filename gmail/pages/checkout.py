from pages.locators import CheckoutPageLocators
from common.waits import DriverWaits


class CheckoutPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver_waits = DriverWaits(self.driver)

    def _is_active_payment_method(self, element):
        element_class = element.get_attribute('class')
        return 'is-active' in element_class

    def get_info_from_checkout_page(self):

        data = {
            'order_summary': {
                'title': self.driver.find_element(*CheckoutPageLocators.COURSE_TITLE).text,
                'price': self.driver.find_element(*CheckoutPageLocators.COURSE_PRICE).text,
            },
            'account_info': {
                'user_email': self.driver.find_element(*CheckoutPageLocators.USER_EMAIL).text,
            },
            'payment_methods': {
                'no_of_methods': len(self.driver.find_elements(*CheckoutPageLocators.PAYMENT_OPTION_TABS)),
                'methods': {
                    'credit_card': {
                        'is_active': self._is_active_payment_method(
                            self.driver.find_element(*CheckoutPageLocators.CREDIT_CARD_TAB)),
                        'label': self.driver.find_element(*CheckoutPageLocators.CREDIT_CARD_LABEL).text
                    },
                    'paypal': {
                        'is_active': self._is_active_payment_method(
                            self.driver.find_element(*CheckoutPageLocators.PAYPAL_TAB)),
                        'label': self.driver.find_element(*CheckoutPageLocators.PAYPAL_LABEL).text
                    },
                },
            },
        }

        return data
