import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure # Make sure to import the logger from config.py


def test_main_page(driver):
    logger.info("Navigating to the main page...")
    driver.get("https://the-internet.herokuapp.com")

    logger.info(f"Current URL: {driver.current_url}")

    assert "The Internet" in driver.title
    logger.info("Main page test passed successfully!")


def test_header_text(driver):
    logger.info("Navigating to the A/B Testing page...")
    driver.get("https://the-internet.herokuapp.com/abtest")

    logger.info(f"Current URL: {driver.current_url}")

    expected_variations = ["A/B Test Control", "A/B Test Variation 1"]

    logger.info(f"Waiting for <h3> tag to contain one of: {expected_variations}")
    try:
        WebDriverWait(driver, 10).until(
            lambda d: any(
                variation in d.find_element(By.TAG_NAME, "h3").text
                for variation in expected_variations
            )
        )
        logger.info(f"One of the expected variations was found in the <h3> tag.")
    except Exception as e:
        logger.error(f"Timeout waiting for text in <h3> tag. Error: {str(e)}")
        logger.info("Page source at the time of failure:")
        logger.info(driver.page_source)
        raise

    header = driver.find_element(By.TAG_NAME, "h3")
    header_text = header.text

    logger.info(f"Header text found: {header_text}")

    assert header_text in expected_variations, (
        f"Header text did not match any expected variation. Got '{header_text}'"
    )
    logger.info("Header text test passed successfully!")
