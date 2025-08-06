import logging
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

timestamp = time.strftime("%Y%m%d-%H%M%S")
log_file_path = os.path.join(log_dir, f"test_log_{timestamp}.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path, mode="w"),
        logging.StreamHandler()
    ],
    force=True
)
logger = logging.getLogger()

def pytest_configure(config):
    logger.info("Initializing pytest logging configuration.")
    for handler in logging.getLogger().handlers:
        if isinstance(handler, logging.FileHandler):
            logger.info(f"Log file: {handler.baseFilename}")

@pytest.fixture(scope="function")
def driver():
    use_grid = os.getenv("USE_SELENIUM_GRID", "false").lower() == "true"
    chrome_options = Options()

    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    prefs = {
        "download.default_directory": "/tmp/selenium_downloads",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "download.extensions_to_open": "applications/pdf,text/plain"
    }
    chrome_options.add_experimental_option("prefs", prefs)

    if use_grid:
        logger.info("Initializing remote WebDriver using Selenium Grid.")
        driver = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            options=chrome_options,
            desired_capabilities=DesiredCapabilities.CHROME
        )
    else:
        logger.info("Initializing local Chrome WebDriver.")
        driver = webdriver.Chrome(options=chrome_options)

    yield driver

    logger.info("Quitting WebDriver...")
    driver.quit()
