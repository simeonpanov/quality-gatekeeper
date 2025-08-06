import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure  # Adjust imports as necessary

@pytest.mark.usefixtures("driver")
def test_nested_frames(driver):
    logger.info("Navigating to the Nested Frames page.")
    driver.get("https://the-internet.herokuapp.com/nested_frames")

    logger.info("Switching to the 'frame-top'.")
    driver.switch_to.frame("frame-top")

    try:
        logger.info("Switching to the 'frame-left'.")
        driver.switch_to.frame("frame-left")
        left_content = driver.find_element(By.TAG_NAME, "body").text
        assert "LEFT" in left_content, "Content of 'frame-left' is incorrect."
        logger.info("Content of 'frame-left' verified.")
    except Exception as e:
        logger.error(f"Error in 'frame-left': {e}")
        raise AssertionError("Error verifying content in 'frame-left'.")
    finally:
        driver.switch_to.parent_frame()

    try:
        logger.info("Switching to the 'frame-middle'.")
        driver.switch_to.frame("frame-middle")
        middle_content = driver.find_element(By.ID, "content").text
        assert "MIDDLE" in middle_content, "Content of 'frame-middle' is incorrect."
        logger.info("Content of 'frame-middle' verified.")
    except Exception as e:
        logger.error(f"Error in 'frame-middle': {e}")
        raise AssertionError("Error verifying content in 'frame-middle'.")
    finally:
        driver.switch_to.parent_frame()

    try:
        logger.info("Switching to the 'frame-right'.")
        driver.switch_to.frame("frame-right")
        right_content = driver.find_element(By.TAG_NAME, "body").text
        assert "RIGHT" in right_content, "Content of 'frame-right' is incorrect."
        logger.info("Content of 'frame-right' verified.")
    except Exception as e:
        logger.error(f"Error in 'frame-right': {e}")
        raise AssertionError("Error verifying content in 'frame-right'.")
    finally:
        driver.switch_to.default_content()

    try:
        logger.info("Switching to the 'frame-bottom'.")
        driver.switch_to.frame("frame-bottom")
        bottom_content = driver.find_element(By.TAG_NAME, "body").text
        assert "BOTTOM" in bottom_content, "Content of 'frame-bottom' is incorrect."
        logger.info("Content of 'frame-bottom' verified.")
    except Exception as e:
        logger.error(f"Error in 'frame-bottom': {e}")
        raise AssertionError("Error verifying content in 'frame-bottom'.")
    finally:
        driver.switch_to.default_content()
