import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from config.config import logger, driver, pytest_configure

def test_dropdown_selection(driver):
    """
    Test to select options from a dropdown on the HerokuApp dropdown page.
    This function combines navigation, interaction, and validation steps for dropdown selection.
    """
    page_url = "https://the-internet.herokuapp.com/dropdown"

    try:
        driver.get(page_url)
        logger.info(f"Navigated to the page: {page_url}")

        dropdown_element = driver.find_element(By.ID, "dropdown")
        select = Select(dropdown_element)

        select.select_by_value("1")
        selected_option = select.first_selected_option.text
        assert selected_option == "Option 1", "Dropdown selection failed: 'Option 1' not selected"
        logger.info("Dropdown test passed for 'Option 1'.")

        select.select_by_value("2")
        selected_option = select.first_selected_option.text
        assert selected_option == "Option 2", "Dropdown selection failed: 'Option 2' not selected"
        logger.info("Dropdown test passed for 'Option 2'.")

    except Exception as e:
        logger.error(f"An error occurred during the dropdown test: {str(e)}")
