# Test Case: Verify Exported Candidate Information from Recruitment ATS Section
from helpers.utils import Utils


# Step 1: TODO - Open the application
# Step 2: TODO - Login
# Step 3: TODO - Go to Recruitment ATS section
# Step 4: TODO - Filter candidates
# Step 5: TODO - Open the filter and fill in the job title "Customer Support Specalist"
# Step 6: TODO - Click on 'Search' button
# Step 7: TODO - Click on 'Export to CSV' button
# Step 8: TODO - Once CSV is exported, open it
# Step 9: TODO - Verify that information from the table in the application corresponds to information in the exported CSV file

def test_verify_exported_candidate_information(app):
    Utils.clear_download_directory()
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Recruitment (ATS)")
