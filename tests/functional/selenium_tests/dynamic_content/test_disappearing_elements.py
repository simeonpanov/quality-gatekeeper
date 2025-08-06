import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import logger, driver, pytest_configure

#Testing Github Actions

def test_disappearing_elements(driver):
    base_url = "https://the-internet.herokuapp.com"
    page_url = f"{base_url}/disappearing_elements"

    try:
        driver.get(page_url)
        logger.info(f"Navigated to the page: {page_url}")

        links = [
            ("Home", f"{base_url}/"),
            ("About", f"{base_url}/about/"),
            ("Contact Us", f"{base_url}/contact-us/"),
            ("Portfolio", f"{base_url}/portfolio/"),
        ]


        for link_text, link_url in links:
            logger.info(f"Navigating to the URL: {link_url}")

            try:
                driver.get(link_url)

                driver.implicitly_wait(5)

                body_text = driver.page_source
                if "Not Found" in body_text:
                    logger.error(f"{link_url} - Page not found (404).")
                else:
                    logger.info(f"Successfully navigated to {link_url} - Page found.")

            except Exception as e:
                logger.error(f"Error occurred while navigating to {link_text} ({link_url}): {str(e)}")

    except Exception as e:
        logger.error(f"An error occurred during the test: {str(e)}")