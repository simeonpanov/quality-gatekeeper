import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure  # Adjust import as necessary

def test_forgot_password(driver):
    logger.info("Navigating to the Forgot Password page.")
    driver.get("https://the-internet.herokuapp.com/forgot_password")

    logger.info("Locating the email input field.")
    email_input = driver.find_element(By.ID, "email")
    assert email_input.is_displayed(), "Email input field should be visible."
    logger.info("Email input field is visible.")

    test_email = "test@example.com"
    logger.info(f"Entering a valid email address: {test_email}")
    email_input.send_keys(test_email)

    logger.info("Clicking the 'Retrieve password' button.")
    submit_button = driver.find_element(By.ID, "form_submit")
    submit_button.click()

    logger.info("Checking if the result is an Internal Server Error.")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Internal Server Error')]"))
        )
        logger.info("Internal Server Error page is displayed as expected.")
    except Exception as e:
        logger.error(f"Error page not detected as expected: {e}")
        raise

    logger.info("Test Passed: Internal Server Error page detected successfully.")
