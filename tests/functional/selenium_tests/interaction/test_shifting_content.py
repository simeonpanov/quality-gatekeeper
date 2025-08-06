from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from config.config import logger, driver, pytest_configure  # Adjust import as necessary

@pytest.mark.usefixtures("driver")
def test_shifting_content(driver):
    logger.info("Navigating to the Shifting Content page.")
    driver.get("https://the-internet.herokuapp.com/shifting_content")

    title_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h3"))
    )
    assert title_element.text == "Shifting Content", "Title 'Shifting Content' not found."

    example_1_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Example 1: Menu Element"))
    )
    assert example_1_link.is_displayed(), "Example 1 link is not visible."

    example_2_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Example 2: An image"))
    )
    assert example_2_link.is_displayed(), "Example 2 link is not visible."

    example_3_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Example 3: List"))
    )
    assert example_3_link.is_displayed(), "Example 3 link is not visible."

    example_1_link.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h3"))
    )
    logger.info("Navigated to Menu Element example.")

    driver.back()

    example_2_link.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h3"))
    )
    logger.info("Navigated to Image example.")

    driver.back()

    example_3_link.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h3"))
    )
    logger.info("Navigated to List example.")

    driver.back()