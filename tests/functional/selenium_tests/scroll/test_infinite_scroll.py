import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure
import time

def test_infinite_scroll(driver):
    logger.info("Opening Infinite Scroll page.")
    driver.get("https://the-internet.herokuapp.com/infinite_scroll")

    initial_content = driver.find_elements(By.CLASS_NAME, "jscroll-added")
    initial_content_count = len(initial_content)
    logger.info(f"Initial content count: {initial_content_count}")

    scroll_attempts = 3
    for attempt in range(scroll_attempts):
        logger.info(f"Scroll attempt {attempt + 1}/{scroll_attempts}")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jscroll-added"))
        )

        time.sleep(2)

    new_content = driver.find_elements(By.CLASS_NAME, "jscroll-added")
    new_content_count = len(new_content)
    logger.info(f"New content count after scrolling: {new_content_count}")

    assert new_content_count > initial_content_count, "Content did not load after scrolling."

    logger.info("Infinite Scroll test passed successfully.")
