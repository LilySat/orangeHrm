# Test Case 6_1: Verify Password Field Required Validation
# Test Name: Test_Password_Field_Required
# Purpose: To verify that the password field shows a 'required' error message when left empty and 'Save' is clicked.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Add User' button.
# 5. Leave the 'Password' and 'Confirm Password' fields empty.
# 6. Click on the 'Save' button to trigger validation.
# Expected Result:
# An error message stating 'Required' should appear under both 'Password' and 'Confirm Password' fields.

# -----------------------------------------------------------------------------------

# Test Case 6_2: Verify Password Minimum Length Validation
# Test Name: Test_Password_Min_Length
# Purpose: To verify that the password field shows a minimum length error message when fewer than 8 characters are entered.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Add User' button.
# 5. Enter a single character in the 'Password' field.
# 6. Click on the 'Save' button to trigger validation.
# Expected Result:
# An error message stating 'Your password must have at least 8 characters.' should appear under the 'Password' field.

# -----------------------------------------------------------------------------------

# Test Case 6_3: Verify Password Strength Indicator - Very Weak
# Test Name: Test_Password_Strength_Very_Weak
# Purpose: To verify that the password strength indicator shows 'Very Weak' when 8 identical characters are entered.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Add User' button.
# 5. Enter '00000000' in the 'Password' field.
# 6. Observe the password strength indicator.
# Expected Result:
# The password strength indicator should display a 'Very Weak' message.

# -----------------------------------------------------------------------------------

# Test Case 6_4: Verify Password Strength Indicator - Weak
# Test Name: Test_Password_Strength_Weak
# Purpose: To verify that the password strength indicator shows 'Weak' when the password is not complex enough.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Add User' button.
# 5. Enter '00000000..' as the password.
# 6. Observe the password strength indicator.
# Expected Result:
# The password strength indicator should display a 'Weak' message.

# -----------------------------------------------------------------------------------

# Test Case 6_5: Verify Password Strength Indicator - Better
# Test Name: Test_Password_Strength_Better
# Purpose: To verify that the password strength indicator shows 'Better' when the password includes an uppercase letter.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Add User' button.
# 5. Enter '00000000A..' as the password.
# 6. Observe the password strength indicator.
# Expected Result:
# The password strength indicator should display a 'Better' message.

# -----------------------------------------------------------------------------------

# Test Case 6_6: Verify Password Strength Indicator - Strongest
# Test Name: Test_Password_Strength_Strongest
# Purpose: To verify that the password strength indicator shows 'Strongest' when the password includes a mix of uppercase letters, lowercase letters, numbers, and special symbols.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Add User' button.
# 5. Enter 'Nydhig-rorpak-9fojsy' as the password.
# 6. Observe the password strength indicator.
# Expected Result:
# The password strength indicator should display a 'Strongest' message.

def test_case_6_1_Test_Password_Field_Required(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.step.specified_element_is_present('div[id="systemUserDiv"]')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.click_on_save
    app.assert_that(app.orangeHrm.popUp.password_required()).is_equal_to('Required')
    app.assert_that(app.orangeHrm.popUp.confirm_password_required()).is_equal_to('Required')

def test_case_6_2_verify_password_minimum_length_validation(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.step.specified_element_is_present('div[id="systemUserDiv"]')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.set_password('1')
    app.assert_that(app.orangeHrm.popUp.password_required()).is_equal_to('Your password should have at least 8 characters.')

def test_case_6_3_verify_password_strength_indicator_very_weak(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.step.specified_element_is_present('div[id="systemUserDiv"]')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.set_password('00000000')
    app.orangeHrm.popUp.set_confirm_password('00000000')
    app.assert_that(app.orangeHrm.popUp.check_strength_indicator()).is_equal_to('Very Weak')

def test_case_6_4_verify_password_strength_indicator_weak(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.step.specified_element_is_present('div[id="systemUserDiv"]')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.set_password('AA000000')
    app.orangeHrm.popUp.set_confirm_password('AA000000')
    app.assert_that(app.orangeHrm.popUp.check_strength_indicator()).is_equal_to('Weak')

def test_case_6_5_verify_password_strength_indicator_better(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.step.specified_element_is_present('div[id="systemUserDiv"]')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.set_password('AAA00000')
    app.orangeHrm.popUp.set_confirm_password('AAA00000')
    app.assert_that(app.orangeHrm.popUp.check_strength_indicator()).is_equal_to('Better')

def test_case_6_6_verify_password_strength_indicator_Strongest(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.step.specified_element_is_present('div[id="systemUserDiv"]')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.set_password('Aa1!Aa1!')
    app.orangeHrm.popUp.set_confirm_password('Aa1!Aa1!')
    app.assert_that(app.orangeHrm.popUp.check_strength_indicator()).is_equal_to('Strongest')
