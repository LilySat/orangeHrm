import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

class HrAdministration:
    add_user_button = "//div[@id='systemUserDiv'] //*[text()='add']"
    filter_icon = "//a[@ng-click='navbar.filter()']"
    popup_message = "div[class ='toast-message']"
    table_header = "thead[ng-if='!listData.staticHeader']"

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def click_add_user(self):
        time.sleep(20)
        self.step.click_on_element(self.add_user_button)

    def click_filter_icon(self):
        self.step.click_on_element(self.filter_icon)

    def confirm_popup_message(self):
        return self.step.get_element_text(self.popup_message)

