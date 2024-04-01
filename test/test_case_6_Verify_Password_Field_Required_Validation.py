# Test Case 6: Verify Password Field Required Validation
# Test Name: Test_Password_Field_Required
# Purpose: To verify that the password field shows a 'required' error message when left empty.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Add User' button.
# 5. Leave the 'Password' and 'Confirm Password' fields empty.
# 6. Click outside the password fields to trigger validation.
# Expected Result:
# An error message stating 'Required' should appear under both 'Password' and 'Confirm Password' fields.


def test_case_6_Test_Password_Field_Required(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.step.specified_element_is_present('div[id="systemUserDiv"]')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.click_on_save
    app.assert_that(app.orangeHrm.popUp.password_required()).is_equal_to('Required')
    app.assert_that(app.orangeHrm.popUp.confirm_password_required()).is_equal_to('Required')
