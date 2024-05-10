# Test Case: Verification of Added Course
from helpers.utils import Utils

# Step 1: TODO - Open the application
# Step 2: TODO - Click on 'Training' from the side menu
# Step 3: TODO - Click on 'Add Course' button
# Step 4: TODO - Add title to the course
# Step 5: TODO - Add coordinator
# Step 6: TODO - Click on 'Save' button
# Step 7: TODO - Go to 'Courses'
# Step 8: TODO - Click on 'Filter' button
# Step 9: TODO - Add the title of the created course in the filter
# Step 10: TODO - Click 'Search'
# Step 11: TODO - Verify that the created course is displayed in the table

random_name = Utils.generate_random_string()
def test_case_27_newly_created_course_is_displayed_in_the_table(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.orangeHrm.sideMenu.click_on_side_menu_button('Training')
    app.orangeHrm.training.click_on_add_course_button()
    app.orangeHrm.training.add_course_title(random_name)
    app.orangeHrm.training.add_coordinator('a')
    app.orangeHrm.training.click_on_save_button()
    app.orangeHrm.training.click_on_go_back_to_courses()
    app.orangeHrm.training.click_on_filter_button()
    app.orangeHrm.training.select_title_name_in_filter(random_name)