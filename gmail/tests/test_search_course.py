from tests.base import UIAutomationBase


class TestSearchCourse(UIAutomationBase):
    login_required = True

    def setUp(self):
        self.courses_page.go_to_all_courses_page()

    def test_search_course(self):
        query_string = 'java'
        self.courses_page.search_course_by_keyword(query_string=query_string)

        selenium_courses = self.courses_page.get_courses()

        assert selenium_courses['no_of_courses'] > 0, 'No course found for selenium'

        print(str(selenium_courses))

        # for course in selenium_courses['courses']:
        #     assert query_string in course['title'].lower()

        assert all(query_string in course['title'].lower() for course in selenium_courses['courses']), 'Selenium must be in the course title'
