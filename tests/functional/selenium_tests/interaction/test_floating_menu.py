from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from config.config import logger, driver, pytest_configure  # Importing the logger from config.py


def test_floating_menu(driver):
    logger.info("Navigating to the floating menu page.")
    driver.get("https://the-internet.herokuapp.com/floating_menu")

    logger.info("Locating the floating menu on the page.")
    menu = driver.find_element(By.ID, "menu")
    assert menu.is_displayed(), "Floating menu should be visible initially."
    logger.info("Floating menu is visible.")

    logger.info("Scrolling down the page to the bottom.")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    assert menu.is_displayed(), "Floating menu should remain visible after scrolling."
    logger.info("Floating menu is still visible after scrolling.")

    logger.info("Validating that menu links are visible and clickable.")
    menu_links = menu.find_elements(By.TAG_NAME, "a")
    for link in menu_links:
        assert link.is_displayed(), f"Link {link.text} should be visible."
        assert link.is_enabled(), f"Link {link.text} should be clickable."
        logger.info(f"Link '{link.text}' is visible and clickable.")

    logger.info("Test Passed: The floating menu is visible and clickable.")