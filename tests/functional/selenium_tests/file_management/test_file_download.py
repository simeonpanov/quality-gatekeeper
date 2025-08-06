import os
import time
import pytest
import shutil
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure


def test_file_downloader(driver):
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

    url = "https://the-internet.herokuapp.com/download"
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".example"))
    )

    download_links = driver.find_elements(By.CSS_SELECTOR, ".example a")

    # Limit the number of files to download (e.g., the first 2 files)
    files_to_download = download_links[:1]  # You can change this number to download more or fewer files

    for link in files_to_download:
        file_name = link.text
        download_url = link.get_attribute("href")
        logger.info(f"Starting download for {file_name} from {download_url}")

        link.click()

        time.sleep(3)  # Sleep for a few seconds to allow the download to complete

        downloaded_file_path = os.path.join(download_dir, file_name)
        if os.path.exists(downloaded_file_path):
            logger.info(f"Downloaded: {file_name}")
            os.remove(downloaded_file_path)  # Optionally remove the file after verifying download
        else:
            logger.info(f"Failed to download: {file_name}")
