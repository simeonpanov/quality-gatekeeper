from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure
import pytest


def test_status_codes(driver):
    driver.get("https://the-internet.herokuapp.com/status_codes")

    status_codes = ["200", "301", "404", "500"]

    for code in status_codes:
        link = driver.find_element(By.LINK_TEXT, code)
        logger.info(f"Clicking on status code: {code}")

        link.click()

        WebDriverWait(driver, 10).until(
            EC.url_contains(f"status_codes/{code}")
        )
        logger.info(f"Page URL is now: {driver.current_url}")

        page_body = driver.find_element(By.TAG_NAME, "body").text
        logger.info(f"Page body: {page_body}")

        expected_message = f"This page returned a {code} status code."
        assert expected_message in page_body, f"Expected message '{expected_message}' in body, but got: {page_body}"

        logger.info(f"Status code {code} test passed.")

        driver.back()
