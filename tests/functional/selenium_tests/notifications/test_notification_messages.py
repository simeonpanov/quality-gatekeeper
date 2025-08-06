import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import logger, driver, pytest_configure  # Adjust imports as necessary
import time


def test_notification_message(driver):
    logger.info("Navigating to the Notification Message page.")
    driver.get("https://the-internet.herokuapp.com/notification_message_rendered")

    time.sleep(3)

    try:
        trigger_link = driver.find_element(By.LINK_TEXT, "Click here")
        trigger_link.click()
        logger.info("Clicked the hyperlink to trigger the notification.")
    except Exception as e:
        logger.error(f"Error clicking the hyperlink: {e}")
        return

    def get_notification_text():
        try:
            notification_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "flash"))
            )
            logger.debug(f"Notification element HTML: {notification_element.get_attribute('outerHTML')}")
            return notification_element.text.strip()
        except Exception as e:
            logger.error(f"Notification element is not visible or not present in the DOM: {e}")
            logger.debug("Full page source:")
            logger.debug(driver.page_source)
            return None

    initial_message = get_notification_text()
    if initial_message is None:
        logger.error("Initial notification message retrieval failed.")

    assert initial_message is not None, "Initial notification message could not be retrieved."



