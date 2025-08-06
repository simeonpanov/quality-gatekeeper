import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure

def test_checkboxes(driver):
    logger.info("Navigating to the Checkboxes Testing page...")
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkbox_1 = driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")
    checkbox_2 = driver.find_element(By.XPATH, "//input[@type='checkbox'][2]")

    assert not checkbox_1.is_selected(), "Checkbox 1 should be unchecked initially."
    logger.info("Checkbox 1 is unchecked initially.")

    assert checkbox_2.is_selected(), "Checkbox 2 should be checked initially."
    logger.info("Checkbox 2 is checked initially.")

    if not checkbox_1.is_selected():
        logger.info("Checking Checkbox 1...")
        checkbox_1.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_selected(checkbox_1))
        logger.info("Checkbox 1 is checked.")

    if checkbox_2.is_selected():
        logger.info("Unchecking Checkbox 2...")
        checkbox_2.click()
        # Wait for checkbox 2 to be unchecked
        WebDriverWait(driver, 10).until(lambda driver: not checkbox_2.is_selected())
        logger.info("Checkbox 2 is unchecked.")

    assert checkbox_1.is_selected(), "Checkbox 1 should be checked."
    logger.info("Verified Checkbox 1 is checked.")

    assert not checkbox_2.is_selected(), "Checkbox 2 should be unchecked."
    logger.info("Verified Checkbox 2 is unchecked.")

    if not checkbox_1.is_selected():
        logger.info("Rechecking Checkbox 1...")
        checkbox_1.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_selected(checkbox_1))
        logger.info("Checkbox 1 is rechecked.")

    if not checkbox_2.is_selected():
        logger.info("Checking Checkbox 2...")
        checkbox_2.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_selected(checkbox_2))
        logger.info("Checkbox 2 is checked.")

    assert checkbox_1.is_selected(), "Checkbox 1 should be checked after rechecking."
    logger.info("Verified Checkbox 1 is checked.")

    assert checkbox_2.is_selected(), "Checkbox 2 should be checked after rechecking."
    logger.info("Verified Checkbox 2 is checked.")