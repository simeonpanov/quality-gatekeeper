import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure


def test_dynamic_controls(driver):
    """
    Test to verify the functionality of dynamic controls.
    This includes adding/removing a checkbox and enabling/disabling an input field.
    """
    page_url = "https://the-internet.herokuapp.com/dynamic_controls"

    try:
        driver.get(page_url)
        logger.info(f"Navigated to the page: {page_url}")

        checkbox_button = driver.find_element(By.CSS_SELECTOR, "#checkbox-example button")
        checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox input")

        checkbox_button.click()
        logger.info("Clicked 'Remove' button for checkbox.")

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "message"), "It's gone!")
        )
        logger.info("Checkbox removed successfully.")

        checkbox_button.click()
        logger.info("Clicked 'Add' button for checkbox.")

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "message"), "It's back!")
        )
        logger.info("Checkbox added successfully.")

        input_button = driver.find_element(By.CSS_SELECTOR, "#input-example button")
        input_field = driver.find_element(By.CSS_SELECTOR, "#input-example input")

        input_button.click()
        logger.info("Clicked 'Enable' button for input field.")

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "message"), "It's enabled!")
        )
        assert input_field.is_enabled(), "Input field is not enabled."
        logger.info("Input field enabled successfully.")

        input_button.click()
        logger.info("Clicked 'Disable' button for input field.")

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "message"), "It's disabled!")
        )
        assert not input_field.is_enabled(), "Input field is not disabled."
        logger.info("Input field disabled successfully.")

    except Exception as e:
        logger.error(f"An error occurred during the dynamic controls test: {str(e)}")