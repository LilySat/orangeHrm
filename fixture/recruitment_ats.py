from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver


class RecruitmentAts:
    add_candidate_button = '//button[@tooltip="Add Candidate"]'


    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def click_add_candidate_button(self):
        self.step.click_on_element(self.add_candidate_button)
