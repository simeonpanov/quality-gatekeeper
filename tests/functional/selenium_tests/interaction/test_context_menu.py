from selenium.webdriver.common.by import By
import requests
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


def test_context_menu(driver):
    url = "https://the-internet.herokuapp.com/context_menu"
    logger.info(f"Navigating to {url}")
    driver.get(url)

    hotspot = driver.find_element(By.ID, "hot-spot")

    logger.info("Right-clicking on the hotspot...")
    action = ActionChains(driver)
    action.context_click(hotspot).perform()

    time.sleep(2)

    alert = Alert(driver)
    alert_text = alert.text
    logger.info(f"Alert text: {alert_text}")

    assert alert_text == "You selected a context menu", f"Expected alert text 'You selected a context menu', but got '{alert_text}'."

    alert.accept()
    logger.info("Alert accepted.")