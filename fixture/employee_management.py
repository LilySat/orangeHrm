from cgitb import text

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

class EmployeeManagement:
    home_button = "a[data-automation-id='menu_home']"
    list_of_widgets_header_texts = ".widget-header span:last-child"
    employment_status_filter = '//label[@for="emp_search_mdl_employee_status_filter"]/preceding-sibling::div'
    list_of_employment_statuses = '#emp_search_mdl_employee_status_filter'
    employee_list_button = '#top_level_menu_item_menu_item_128'
    employee_list_filter_button = '//a[@ng-click="navbar.filter()"]'
    location_input_field = '//label[@for="emp_search_mdl_employee_location_filter"]/preceding-sibling::div'
    list_of_locations = '#emp_search_mdl_employee_location'


    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def click_home(self):
        self.step.click_on_element(self.home_button)

    def get_widgets_headers(self):
        return self.step.get_elements_texts(self.list_of_widgets_header_texts)

    def choose_employment_status_in_filter(self):
        self.step.click_on_element(self.employment_status_filter)
        self.step.click_element_by_text(self.list_of_employment_statuses, text)

    def navigate_to_employee_list_filter(self):
        self.step.click_on_element(self.employee_list_button)
        self.step.click_on_element(self.employee_list_filter_button)

