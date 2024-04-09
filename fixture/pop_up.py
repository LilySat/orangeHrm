from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver


class PopUp:
    user_name_field = '#systemuser_uname_filter'
    employee_name_field = '#employee_name_filter_value'
    password_field = '#password'
    confirm_password_field = '#confirmpassword'
    save_button = '#modal-save-button'
    user_exists_error_massage = "//span[text()='Already exists']"
    user_name_filter_field = '//input[@id="systemuser_uname_filter"]'
    filter_popup_table = '//div[@class="modal modal-fixed-footer open"]//h4[text()="Filter Users"]'
    filter_search_button = '//div[@class="modal modal-fixed-footer open"]//a[text()="Search"]'
    pass_required_message = '#password+span'
    confirm_pass_required_message = '#confirmpassword+span'
    pass_strength_message = '.password-strength-check'
    empty_space = '.password-help-text-container small'
    spinner = '.oxd-circle-loader'
    employee_name_dropdown = '#employee_name_filter_dropdown'
    employee_name_dropdown_first_line = '//*[@id="employee_name_filter_dropdown"]/div[3]'
    employee_name_no_results = '//*[@id="employee_name_filter_dropdown"]/div[2]'

    ess_role_field = '//*[text()="ESS Role"]/preceding-sibling::div'
    ess_role_dropdown_option = '//*[@class="select-wrapper initialized"]//span[text()="Default ESS"]'
    ess_dropdown = '//label[text()="ESS Role"]/..//ul/li'
    admin_role_field = '//*[text()="Admin Role"]/preceding-sibling::div'
    admin_role_dropdown_option = '//*[@class="select-wrapper initialized"]//span[text()="Global Admin"]'
    supervisor_role_field = '//*[text()="Supervisor Role"]/preceding-sibling::div'
    supervisor_role_dropdown_option = '//*[@class="select-wrapper initialized"]//span[text()="Default Supervisor"]'
    status_field = '//*[text()="Status"]/preceding-sibling::div'
    status_dropdown_option = '//*[@class="select-wrapper initialized"]//span[text()="Enabled"]'
    location_field = '//*[text()="Location"]/preceding-sibling::div'
    location_first_option_in_dropdown = '//*[@class="select-wrapper initialized"]//span[text()="Australia"]'
    cancel_button_in_filter_popup = '//a[@class="modal-action modal-close waves-effect btn"][text()="Cancel"]'


    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def set_username(self, text):
        self.step.click_on_element(self.user_name_field)
        self.step.input_text(self.user_name_field, text)

    def set_employee_name(self, text):
        self.step.input_text(self.employee_name_field, text)

    def set_password(self, text):
        self.step.click_on_element(self.password_field)
        self.step.input_text(self.password_field, text)

    def set_confirm_password(self, text):
        self.step.input_text(self.confirm_password_field, text)

    def click_on_save(self):
        self.step.click_on_element(self.save_button)

    def get_user_exist_error(self):
        return self.step.get_element_text(self.user_exists_error_massage)

    def click_on_search(self):
        self.step.click_on_element(self.filter_search_button)

    def password_required(self):
        return self.step.get_element_text(self.pass_required_message)

    def confirm_password_required(self):
        return self.step.get_element_text(self.confirm_pass_required_message)

    def check_strength_indicator(self):
        return self.step.get_element_text(self.pass_strength_message)

    def click_empty_space(self):
        self.step.click_on_element(self.empty_space)

    def start_typing_employee_name(self, text):
        self.step.click_on_element(self.employee_name_field)
        self.step.input_text(self.employee_name_field, text)

    def confirm_employee_name_dropdown(self):
        self.step.specified_element_is_present(self.employee_name_dropdown)
        return self.step.get_element_text(self.employee_name_dropdown_first_line).lower()

    def confirm_employee_name_no_results(self):
        self.step.specified_element_is_present(self.employee_name_dropdown)
        return self.step.get_element_text(self.employee_name_no_results)

    def select_ess_role_dropdown_option(self):
        self.step.click_on_element(self.ess_role_field)
        self.step.click_on_element(self.ess_role_dropdown_option)

    def select_admin_role_dropdown_option(self):
        self.step.click_on_element(self.admin_role_field)
        self.step.click_on_element(self.admin_role_dropdown_option)

    def select_supervisor_role_dropdown_option(self):
        self.step.click_on_element(self.supervisor_role_field)
        self.step.click_on_element(self.supervisor_role_dropdown_option)

    def select_status_dropdown_option(self):
        self.step.click_on_element(self.status_field)
        self.step.click_on_element(self.status_dropdown_option)

    def select_location_dropdown_option(self):
        self.step.click_on_element(self.location_field)
        self.step.click_on_element(self.location_first_option_in_dropdown)

    def set_employee_name(self, text):
        self.step.input_text(self.employee_name_field, text)

    def click_cancel_button(self):
        self.step.click_on_element(self.cancel_button_in_filter_popup)

    def select_value_in_dropdown(self):
        self.step.select_dropdown_by_text(self.employee_name_dropdown)

    def click_on_ess_role_input_field(self):
        self.step.click_on_element(self.ess_role_field)