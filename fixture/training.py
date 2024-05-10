from cgitb import text

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver
from fixture.table import Table


class Training:
    filter_button = "a[id=searchModal]"
    add_course_button = "#addItemBtn"
    iframe = "#noncoreIframe"
    courses_list_table = "#search-results"
    add_course_header = "#addCourseTitle"
    title_input_field = "#addCourse_title"
    coordinator_input_field = "#addCourse_coordinator_empName"
    results_dropdown = "//div[@class='ac_results']"
    first_result_in_coordinator_dropdown = "//div[@class='ac_results']//li[1]"
    save_button = "#btnSaveCourse"
    go_back_to_couses = "//a[@data-automation-id='menu_back']"
    success_popup = "#toast-container"
    filter_button = "//a[@data-tooltip='Filter']"
    title_name_in_filter = "//input[@name='searchCourse[title]']"

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table = Table(step,
                           row_selector='#resultTable tbody tr',
                           column_selectors={'check_box_list': '#resultTable td:nth-child(1)',
                                             'title': '#resultTable td:nth-child(2) a',
                                             'subunit': '#resultTable td:nth-child(3) a',
                                             'coordinator': '#resultTable td:nth-child(4) a',
                                             'company': '#resultTable td:nth-child(5) a',
                                             'status': '#resultTable td:nth-child(6) a'})

    def click_on_filter_button(self):
        self.step.switch_to_iframe(self.iframe)
        self.step.click_on_element(self.filter_button)
        self.step.switch_to_default_content()

    def click_on_add_course_button(self):
        self.step.wait_for_element(self.add_course_button)
        self.step.click_on_element(self.add_course_button)

    def add_course_title(self):
        self.step.wait_for_element(self.add_course_header)
        self.step.input_text(self.title_input_field, text)

    def add_coordinator(self):
        self.step.input_text(self.coordinator_input_field, text)
        self.step.wait_for_element(self.results_dropdown)
        self.step.click_on_element(self.first_result_in_coordinator_dropdown)

    def click_on_save_button(self):
        self.step.click_on_element(self.save_button)

    def click_on_go_back_to_courses(self):
        self.step.wait_for_element(self.success_popup)
        self.step.click_on_element(self.go_back_to_couses)

    def click_on_filter_button(self):
        self.step.click_on_element(self.filter_button)

    def select_title_name_in_filter(self):
        self.step.input_text(self.title_name_in_filter, text)
        self.step.wait_for_element(self.results_dropdown)
        self.step.click_element_by_text(self.results_dropdown, text)