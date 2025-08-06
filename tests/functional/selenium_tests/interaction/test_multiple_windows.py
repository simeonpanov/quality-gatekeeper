import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure  # Adjust imports as necessary

@pytest.mark.usefixtures("driver")
def test_open_new_window(driver):
    logger.info("Navigating to the page with new window functionality.")
    driver.get("https://the-internet.herokuapp.com/windows")

    logger.info("Verifying the presence of the 'Click Here' link.")
    try:
        click_here_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Click Here"))
        )
        assert click_here_link.is_displayed(), "'Click Here' link is not visible."
        logger.info("'Click Here' link is visible.")
    except Exception as e:
        logger.error(f"Error finding 'Click Here' link: {e}")
        raise AssertionError("'Click Here' link was not found or not visible.")

    original_window = driver.current_window_handle
    logger.info("Clicking the 'Click Here' link to open a new window.")
    click_here_link.click()

    WebDriverWait(driver, 10).until(EC.new_window_is_opened)
    new_window_handle = None

    for handle in driver.window_handles:
        if handle != original_window:
            new_window_handle = handle
            break

    if not new_window_handle:
        logger.error("New window did not open.")
        raise AssertionError("New window did not open.")

    logger.info("Switching to the new window.")
    driver.switch_to.window(new_window_handle)

    try:
        new_window_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h3"))
        )
        assert new_window_header.is_displayed(), "Header in the new window is not visible."
        assert new_window_header.text == "New Window", "Header text in the new window is incorrect."
        logger.info("New window content verified successfully.")
    except Exception as e:
        logger.error(f"Error verifying content in the new window: {e}")
        raise AssertionError("New window content verification failed.")

    logger.info("Switching back to the original window.")
    driver.switch_to.window(original_window)

    try:
        original_window_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h3"))
        )
        assert original_window_header.is_displayed(), "Original window header is not visible after switching back."
        assert original_window_header.text == "Opening a new window", "Original window header text is incorrect after switching back."
        logger.info("Switched back to the original window successfully.")
    except Exception as e:
        logger.error(f"Error verifying content in the original window after switch: {e}")
        raise AssertionError("Original window content verification failed after switching back.")
