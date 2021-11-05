import unittest

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.courses import CoursesPage
from pages.main_nav import MainNavigation


class UIAutomationBase(unittest.TestCase):

    login_required = False

    driver = None
    home_page = None
    login_page = None
    courses_page = None
    main_navigation = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.courses_page = CoursesPage(cls.driver)
        cls.main_navigation = MainNavigation(cls.driver)

        cls.home_page.load_home_page()

        if cls.login_required:
            cls.login_page.login()

    @classmethod
    def tearDownClass(cls):

        if cls.login_required:
            cls.main_navigation.logout()

        cls.driver.quit()
