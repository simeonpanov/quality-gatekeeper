import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure  # Make sure to import the logger from config.py


@pytest.mark.run(order=3)
def test_add_or_remove_elements(driver):
    logger.info("Navigating to the Add or Remove Elements Testing page...")
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    logger.info(f"Current URL: {driver.current_url}")

    logger.info("Waiting for 'Add Element' button to be clickable...")
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Element']"))
    )
    logger.info("'Add Element' button found, clicking it...")
    add_button.click()

    logger.info("Clicking the 'Delete' button on the newly added element...")

    delete_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "added-manually"))
    )
    logger.info("'Delete' button found, clicking it...")
    delete_button.click()

    logger.info("Add/Remove elements test passed successfully!")

    logger.info(f"Current URL after interaction: {driver.current_url}")
