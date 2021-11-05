import time

from selenium.webdriver.common.keys import Keys

from pages.locators import MainNavLocators
from pages.locators import CoursesPageLocators
from common.waits import DriverWaits


class CoursesPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver_waits = DriverWaits(self.driver)

    def go_to_all_courses_page(self):
        self.driver.find_element(*MainNavLocators.ALL_COURSES_LINK).click()
        self.driver_waits.wait_till_element_is_visible(CoursesPageLocators.COURSE_DIRECTORY)

    def get_courses(self):
        courses = {
            'no_of_courses': 0,
            'courses': [],
        }
        course_elements = self.driver.find_elements(*CoursesPageLocators.COURSE_BLOCK)
        courses['no_of_courses'] = len(course_elements)

        for course_element in course_elements:
            course_title = course_element.find_element(*CoursesPageLocators.COURSE_TITLE).text
            course_price = course_element.find_element(*CoursesPageLocators.COURSE_PRICE).text

            course_details = {
                'title': course_title,
                'price': course_price
            }

            courses['courses'].append(course_details)

        return courses

    def search_course_by_keyword(self, query_string=''):
        search_box = self.driver.find_element(*CoursesPageLocators.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(query_string)
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)
