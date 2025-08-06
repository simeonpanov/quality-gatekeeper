import pytest
from config.config import logger, driver, pytest_configure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_tinymce_readonly_mode(driver):
    logger.info("Test started")

    driver.get('https://the-internet.herokuapp.com/tinymce')
    logger.info("Navigated to the TinyMCE page")

    iframe = driver.find_element(By.ID, "mce_0_ifr")
    driver.switch_to.frame(iframe)

    editor_body = driver.find_element(By.CSS_SELECTOR, "body")

    assert editor_body is not None, "Editor body is not found"
    logger.info("Editor body exists")

    is_read_only = editor_body.get_attribute("contenteditable") == "false"
    assert is_read_only, "Editor is not in read-only mode"
    logger.info("Editor is in read-only mode")

    driver.quit()
    logger.info("Test finished and browser closed")