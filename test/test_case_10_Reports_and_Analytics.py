# Test case 10 - verify folders creation functionality
# Open the application
# Login
# Click on Reports and Analytics
# Click on New Folder
# Fill in the folder name
# Click Save
# Verify that New Folder appeared in the list of folders

from helpers.utils import Utils


random_name = Utils.generate_random_string()
def test_case_10_verify_folder_creation_functionality(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button("Reports and Analytics")
    app.orangeHrm.reportsAndAnalytics.click_new_folder_button()
    app.orangeHrm.reportsAndAnalytics.type_new_folder_name(random_name)
    app.orangeHrm.reportsAndAnalytics.click_save_button()
    app.orangeHrm.reportsAndAnalytics.get_pop_up_message()
    app.assert_that(app.orangeHrm.reportsAndAnalytics.get_folder_names()).contains(random_name)