import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure  # Import logger and driver from config
import re

def test_geolocation(driver):
    logger.info("Opening Geolocation page.")
    driver.get("https://the-internet.herokuapp.com/geolocation")

    logger.info("Clicking the 'Where am I?' button.")
    button = driver.find_element(By.XPATH, "//button[contains(text(), 'Where am I?')]")
    button.click()

    logger.info("Waiting for the geolocation data to appear.")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lat-value")))

    latitude = driver.find_element(By.ID, "lat-value").text
    longitude = driver.find_element(By.ID, "long-value").text

    logger.info(f"Latitude: {latitude}")
    logger.info(f"Longitude: {longitude}")

    coordinate_pattern = r"^-?\d+(\.\d+)?$"

    assert re.match(coordinate_pattern, latitude), f"Invalid latitude format: {latitude}"
    assert re.match(coordinate_pattern, longitude), f"Invalid longitude format: {longitude}"

    logger.info("Geolocation test passed successfully.")
