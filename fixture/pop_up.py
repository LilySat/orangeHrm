import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver


class PopUp:
    user_name_field = '#user_name'
    employee_name_field = '#selectedEmployee_value'
    password_field = '#password'
    confirm_password_field = '#confirmpassword'
    save_button = '#modal-save-button'
    user_exists_error_massage = "//span[text()='Already exists']"
    filter_username_field = "//input[@id='systemuser_uname_filter']"
    search_button = "//a[@ng-click='modal.search()']"
    admin_user = "tbody td:nth-child(2) span"
    password_error = "//input[@id='password']/following-sibling::span"
    confirm_password_error = "//input[@id='confirmpassword']/following-sibling::span"
    strength_indicator = "span[class ='password-strength-check']"

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def set_username(self, text):
        self.step.input_text(self.user_name_field, text)

    def set_employee_name(self, text):
        self.step.input_text(self.employee_name_field, text)

    def set_password(self, text):
        self.step.input_text(self.password_field, text)

    def set_confirm_password(self, text):
        self.step.input_text(self.confirm_password_field, text)

    def click_on_save(self):
        time.sleep(20)
        self.step.click_on_element(self.save_button)

    def get_user_exist_error(self):
        return self.step.get_element_text(self.user_exists_error_massage)

    def add_filter_username(self, text):
        self.step.input_text(self.filter_username_field, text)

    def click_on_username_field(self):
        self.step.click_on_element(self.filter_username_field)

    def click_on_search(self):
        self.step.click_on_element(self.search_button)

    def user_admin_exist(self):
        return self.step.get_element_text(self.admin_user)

    def password_required(self):
        return self.step.get_element_text(self.password_error)

    def confirm_password_required(self):
        return self.step.get_element_text(self.confirm_password_error)

    def check_strength_indicator(self):
        time.sleep(5)
        return self.step.get_element_text(self.strength_indicator)
