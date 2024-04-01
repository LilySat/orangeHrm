# Test Case 7: Verify Password Minimum Length Validation
# Test Name: Test_Password_Min_Length
# Purpose: To verify that the password field shows a minimum length error message when fewer than 8 characters are entered.
# Steps:
# 1. Follow steps 1-4 from Test Case 6.
# 2. Enter a single character in the 'Password' field.
# 3. Click outside the password field to trigger validation.
# Expected Result:
# An error message stating 'Your password must have at least 8 characters.' should appear under the 'Password' field.


def test_case_7_verify_password_minimum_length_validation(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.step.specified_element_is_present('div[id="systemUserDiv"]')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.set_password('1')
    app.assert_that(app.orangeHrm.popUp.password_required()).is_equal_to('Your password should have at least 8 characters.')
