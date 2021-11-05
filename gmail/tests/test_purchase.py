import random
import time

from tests.base import UIAutomationBase


class TestPurchase(UIAutomationBase):
    login_required = True

    def tearDown(self):
        self.main_navigation.go_to_home()

    def test_validate_data_in_purchase_page(self):
        """
        Validate all important data in checkout page
        :return:
        """
        self.main_navigation.go_to_all_courses_page()

        courses_data = self.courses_page.get_courses()

        course_info = random.choice(courses_data['courses'])

        self.courses_page.go_to_course_details_page(course_info['course_id'])
        self.course_details_page.go_for_enroll()

        time.sleep(2)

        checkout_data = self.checkout_page.get_info_from_checkout_page()

        assert course_info['title'].lower() in checkout_data['order_summary']['title'].lower(), 'expected: {}, actual: {}'.format(
            course_info['title'], checkout_data['order_summary']['title']
        )
        assert course_info['price'] == checkout_data['order_summary']['price']

        assert self.credentials['email'] == checkout_data['account_info']['user_email']

        assert checkout_data['payment_methods']['no_of_methods'] == 2

        assert checkout_data['payment_methods']['methods']['credit_card']['is_active']
        assert checkout_data['payment_methods']['methods']['credit_card']['label'] == 'CREDIT CARD'

        assert not checkout_data['payment_methods']['methods']['paypal']['is_active']
        assert checkout_data['payment_methods']['methods']['paypal']['label'] == 'PAYPAL'

