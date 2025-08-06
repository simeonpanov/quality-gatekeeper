import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure


def test_entry_ad(driver):
    """
    Simplified test to verify and close the entry ad modal on the initial page load.
    """
    page_url = "https://the-internet.herokuapp.com/entry_ad"

    try:
        driver.get(page_url)
        logger.info(f"Navigated to: {page_url}")

        # Wait for the modal to appear
        modal = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "modal"))
        )
        logger.info("Ad modal is visible on the initial page load.")

        # Close the modal
        close_button = modal.find_element(By.CSS_SELECTOR, ".modal-footer p")

        try:
            close_button.click()
            logger.info("Clicked the ad modal close button.")
        except Exception as e:
            logger.warning("Click intercepted, using JavaScript click instead.")
            driver.execute_script("arguments[0].click();", close_button)

        # Wait for the modal to become invisible
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "modal"))
        )
        logger.info("Ad modal successfully closed.")

    except Exception as e:
        logger.error(f"An error occurred while testing the Entry Ad: {str(e)}")
        raise
