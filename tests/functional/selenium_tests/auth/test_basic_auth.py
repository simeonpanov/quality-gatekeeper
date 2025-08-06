from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure

def test_basic_auth(driver):
    username = "admin"
    password = "admin"
    url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"

    driver.get(url)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    assert "Congratulations" in driver.page_source

