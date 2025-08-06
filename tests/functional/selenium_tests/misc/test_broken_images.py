from selenium.webdriver.common.by import By
import requests
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure  # Make sure to import the logger from config.py

def test_broken_images(driver):
    logger.info("Navigating to the Add or Remove Elements Testing page...")
    driver.get("https://the-internet.herokuapp.com/broken_images")

    images = driver.find_elements(By.TAG_NAME, 'img')

    broken_images = []

    for img in images:
        img_url = img.get_attribute('src')

        if not img_url:
            logger.info("Image has no src attribute")
            broken_images.append(img)
            continue

        try:
            response = requests.get(img_url)

            if response.status_code != 200:
                logger.info(f"Broken Image found: {img_url} (Status code: {response.status_code})")
                broken_images.append(img)
        except requests.exceptions.RequestException as e:
            logger.info(f"Error checking image: {img_url} - {e}")
            broken_images.append(img)

    if broken_images:
        logger.info(f"{len(broken_images)} broken images found.")
    else:
        logger.info("No broken images found.")
