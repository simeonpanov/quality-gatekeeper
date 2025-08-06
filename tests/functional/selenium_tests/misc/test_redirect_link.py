import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure


@pytest.mark.usefixtures("driver")
def test_redirect_functionality(driver):
    logger.info("Navigating to the Redirection page.")
    driver.get("https://the-internet.herokuapp.com/redirector")

    try:
        redirect_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "redirect"))
        )
        redirect_link.click()
        logger.info("Clicked the redirect link.")
    except Exception as e:
        logger.error(f"Error clicking the redirect link: {e}")
        logger.debug("Full page source:")
        logger.debug(driver.page_source)
        return

    try:
        WebDriverWait(driver, 10).until(
            EC.url_contains("/status_codes")
        )
        current_url = driver.current_url
        logger.info(f"Successfully redirected to the URL: {current_url}")
    except Exception as e:
        logger.error(f"Redirection did not complete successfully: {e}")
        logger.debug("Full page source after redirection:")
        logger.debug(driver.page_source)
        return

    expected_url = "https://the-internet.herokuapp.com/status_codes"
    assert expected_url in current_url, f"Redirection failed. Expected URL: {expected_url}, but got {current_url}"
