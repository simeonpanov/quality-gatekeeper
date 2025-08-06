import os
import time
import pytest
import shutil
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure  # Importing the logger from config.py


def test_file_uploader(driver):
    url = "https://the-internet.herokuapp.com/upload"
    logger.info(f"Navigating to {url}")
    driver.get(url)

    file_path = os.path.abspath("sample_upload_file.txt")  # Make sure this file exists in your test directory
    logger.info(f"Using file path for upload: {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"File does not exist: {file_path}")
        pytest.fail(f"File does not exist: {file_path}")
    else:
        logger.info(f"File found: {file_path}")

    try:
        file_input = driver.find_element(By.ID, "file-upload")
        file_input.send_keys(file_path)  # Upload the file by sending the file path
        logger.info(f"File sent to upload input: {file_path}")
    except Exception as e:
        logger.error(f"Failed to locate or upload file: {e}")
        pytest.fail(f"Failed to locate or upload file: {e}")

    try:
        upload_button = driver.find_element(By.ID, "file-submit")
        upload_button.click()
        logger.info("Clicked the 'Upload' button")
    except Exception as e:
        logger.error(f"Failed to click the upload button: {e}")
        pytest.fail(f"Failed to click the upload button: {e}")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "uploaded-files"))
        )
        logger.info("Upload confirmation found on the page.")
    except Exception as e:
        logger.error(f"Upload confirmation not found: {e}")
        pytest.fail(f"Upload confirmation not found: {e}")

    try:
        uploaded_file_name = driver.find_element(By.ID, "uploaded-files").text
        assert "sample_upload_file.txt" in uploaded_file_name, f"Uploaded file name does not match: {uploaded_file_name}"
        logger.info(f"File uploaded successfully with correct name: {uploaded_file_name}")
    except AssertionError as e:
        logger.error(e)
        pytest.fail(str(e))
    except Exception as e:
        logger.error(f"Error verifying uploaded file name: {e}")
        pytest.fail(f"Error verifying uploaded file name: {e}")


