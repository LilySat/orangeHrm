# Test Case 4: Verify that a user can be filtered by username
# Steps:
# 1. Navigate to the "HR Administration" section in the OrangeHRM application.
# 2. Click on the "Filter" icon/button.
# 3. Enter the username of an existing user in the Username field.
# 4. Click on the "Search" button.
# Expected Result:
# The system should filter out and display only the user(s) matching the entered username.

def test_case_4_verify_that_user_can_be_filtered_by_username(app):
    app.orangeHrm.openUrl("https://portnov_admin-trials711.orangehrmlive.com/client/#/dashboard")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_filter_icon()
    app.orangeHrm.hrAdministration.click_filter_icon()
    app.orangeHrm.popUp.click_on_username_field()
    app.orangeHrm.popUp.add_filter_username('Admin')
    app.orangeHrm.popUp.click_on_search()
    app.assert_that(app.orangeHrm.popUp.user_admin_exist()).is_equal_to('admin')
