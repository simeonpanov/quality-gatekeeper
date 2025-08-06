import os
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure  # Importing the logger from config.py


def test_jquery_ui_menu(driver):
    download_dir = os.path.expanduser("~/Downloads/selenium_downloads")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        logger.info(f"Directory {download_dir} created.")

    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }
    driver.execute_cdp_cmd('Page.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': download_dir})

    logger.info("Opening JQueryUI Menu page.")
    driver.get("https://the-internet.herokuapp.com/jqueryui/menu")

    def reset_menu_state():
        driver.find_element(By.XPATH, "//body").click()
        time.sleep(0.5)  # Give a moment for the menu to reset
        logger.info("Menu state reset by clicking outside.")

    def open_downloads_submenu():
        enabled_menu = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//li[@id='ui-id-3']/a[text()='Enabled']"))
        )
        ActionChains(driver).move_to_element(enabled_menu).perform()
        logger.info("Hovering over the 'Enabled' menu.")
        ActionChains(driver).move_to_element(enabled_menu).click().perform()

        downloads_menu = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//li[@id='ui-id-4']/a[text()='Downloads']"))
        )
        logger.info("Clicking on the 'Downloads' submenu.")
        ActionChains(driver).move_to_element(downloads_menu).click().perform()

    download_links = [
        {"name": "PDF", "xpath": "//li[@id='ui-id-5']/a[text()='PDF']", "file_name": "menu.pdf"},
        {"name": "CSV", "xpath": "//li[@id='ui-id-6']/a[text()='CSV']", "file_name": "menu.csv"},
        {"name": "Excel", "xpath": "//li[@id='ui-id-7']/a[text()='Excel']", "file_name": "menu.xls"}
    ]

    for link in download_links:
        open_downloads_submenu()
        logger.info(f"Clicking on the '{link['name']}' option.")
        option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, link['xpath']))
        )
        option.click()
        time.sleep(2)
        reset_menu_state()

    logger.info("Clicking on the 'Back to JQuery UI' option.")
    open_downloads_submenu()