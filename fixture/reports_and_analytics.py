from cgitb import text

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

from fixture.table import Table


class ReportsAndAnalytics:
    main_page_spinner = '//div[@class="oxd-loading-spinner"]'
    new_folder_button = '//button[@tooltip="New Folder"]'
    new_folder_name_input_field = '//input[@placeholder="Enter Folder Name"]'
    save_button = '//button[@type="submit"]'
    list_of_items_in_the_table = '//div[@class="oxd-accordion"] //p[@class="oxd-text oxd-text--p"]'
    success_pop_up = '//p[@class="oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text"]'


    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def click_new_folder_button(self):
        self.step.specified_element_is_present(self.new_folder_button)
        self.step.click_on_element(self.new_folder_button)

    def type_new_folder_name(self, text):
        self.step.input_text(self.new_folder_name_input_field, text)

    def click_save_button(self):
        self.step.click_on_element(self.save_button)

    def get_pop_up_message(self):
        self.step.wait_for_element(self.success_pop_up)

    def get_folder_names(self):
        self.step.specified_element_is_present(self.list_of_items_in_the_table)
        return self.step.get_elements_texts(self.list_of_items_in_the_table)