import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure
import pytest

@pytest.mark.usefixtures("driver")
def test_slow_resources(driver):
    logger.info("Navigating to the Slow Resources page.")
    driver.get("https://the-internet.herokuapp.com/slow")

    title_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h3"))
    )
    assert title_element.text == "Slow Resources", "Title 'Slow Resources' not found."

    logger.info("Waiting for slow resource to load...")
    time.sleep(30)

    paragraph_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='example']/p"))
    )
    assert paragraph_text.is_displayed(), "Paragraph text is not visible."

    fork_me_image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a/img"))
    )
    assert fork_me_image.is_displayed(), "GitHub image is not visible."

    footer_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@style='text-align: center;']"))
    )
    assert footer_text.is_displayed(), "Footer text is not visible."