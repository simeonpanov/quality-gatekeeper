import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure


@pytest.mark.usefixtures("driver")
def test_shadow_dom_content(driver):
    logger.info("Navigating to the Shadow DOM page.")
    driver.get("https://the-internet.herokuapp.com/shadowdom")

    shadow_host = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "my-paragraph"))
    )
    assert shadow_host is not None, "Shadow host not found on the page."

    shadow_root = shadow_host.shadow_root

    shadow_element = WebDriverWait(shadow_root, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p"))
    )

    shadow_text = shadow_element.text
    logger.info(f"Shadow DOM content: {shadow_text}")
    assert shadow_text == "Let's have some different text!", \
        f"Expected 'Let's have some different text!', but got '{shadow_text}'"
