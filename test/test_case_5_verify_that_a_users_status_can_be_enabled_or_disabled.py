# Test Case 3: Verify that a user's status can be enabled or disabled
# Steps:
# 1. Navigate to the "HR Administration" section in the OrangeHRM application.
# 2. Click on the "Filter" icon/button.
# 3. Enter the username of non-existing user in the Username field.
# 4. Click on the "Search" button.
# Expected Result:
# The system should filter out and display empty list of users.
# The Message: 'No Records Found' should be displayed.

def test_case_5_verify_that_user_status_can_be_enabled_or_disabled(app):
    app.orangeHrm.openUrl("https://portnov_administrator-trials712.orangehrmlive.com")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.step.specified_element_is_present(app.orangeHrm.hrAdministration.table_header, 30)
    app.orangeHrm.hrAdministration.click_filter_icon()
    app.orangeHrm.popUp.click_on_username_field()
    app.orangeHrm.popUp.add_filter_username('NotAnAdmin')
    app.orangeHrm.popUp.click_on_search()
    app.assert_that(app.orangeHrm.popUp.confirm_popup_message()).is_equal_to('No Records Found')
