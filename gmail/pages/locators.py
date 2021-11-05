from selenium.webdriver.common.by import By

class HomePageLocators(object):

    MAIN_BLOCK = (By.CLASS_NAME, 'view-school')


class MainNavLocators(object):

    LOGIN_LINK = (By.CSS_SELECTOR, 'a[href="/sign_in"]')
    MY_PROFILE_ICON = (By.CLASS_NAME, 'open-my-profile-dropdown')
    ALL_COURSES_LINK = (By.CSS_SELECTOR, 'a[href="/courses"]')
    LOGOUT_LINK = (By.CSS_SELECTOR, 'a[href="/sign_out"]')


class LoginPageLocators(object):

    LOGIN_BUTTON = (By.CLASS_NAME, 'login-button')
    EMAIL_INPUT = (By.ID, 'user_email')
    PASSWORD_INPUT = (By.ID, 'user_password')


class CoursesPageLocators(object):
    COURSE_DIRECTORY = (By.CLASS_NAME, 'course-directory')
    COURSE_BLOCK = (By.CLASS_NAME, 'course-listing')
    COURSE_TITLE = (By.CLASS_NAME, 'course-listing-title')
    COURSE_PRICE = (By.CLASS_NAME, 'course-price')
    SEARCH_BOX = (By.ID, 'search-courses')

