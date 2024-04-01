# Test Case 10: Verify Password Strength Indicator - Better
# Test Name: Test_Password_Strength_Better
# Purpose: To verify that the password strength indicator shows 'Better' when the password includes three uppercase letters.
# Steps:
# 1. Follow steps 1-4 from Test Case 6.
# 2. Enter 'AAA00000' in the 'Password' field.
# 3. Observe the password strength indicator.
# Expected Result:
# The password strength indicator should display a 'Better' message.


def test_case_10_verify_password_strength_indicator_better(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.step.specified_element_is_present('div[id="systemUserDiv"]')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.set_password('AAA00000')
    app.orangeHrm.popUp.set_confirm_password('AAA00000')
    app.assert_that(app.orangeHrm.popUp.check_strength_indicator()).is_equal_to('Better')