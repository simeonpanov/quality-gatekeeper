from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure
import pytest


def test_typos(driver):
    driver.get("https://the-internet.herokuapp.com/typos")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "p"))
    )

    correct_text = "Sometimes you'll see a typo, other times you won't."

    typo_found = False
    for _ in range(5):
        page_text = driver.find_element(By.XPATH, "//div[@id='content']//p[2]").text
        logger.info(f"Page text: {page_text}")

        if page_text != correct_text:  # Check if there's a typo
            logger.warning(f"Typo found in page text: {page_text}")
            typo_found = True
            break

        logger.info("No typo found, refreshing the page to check again.")
        driver.refresh()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "p"))
        )

    assert typo_found, "No typo was found after multiple attempts."

    logger.info("Test passed: Typo detected successfully.")
