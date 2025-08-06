import requests
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure

def test_digest_auth(driver):
    url = "https://the-internet.herokuapp.com/digest_auth"

    auth_url = f"https://admin:admin@the-internet.herokuapp.com/digest_auth"
    driver.get(auth_url)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))

    assert "Congratulations" in driver.page_source
    logger.info("Digest Authentication test passed successfully!")