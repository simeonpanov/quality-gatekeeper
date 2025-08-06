import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure


def test_horizontal_slider(driver):
    logger.info("Opening Horizontal Slider page.")
    driver.get("https://the-internet.herokuapp.com/horizontal_slider")

    slider = driver.find_element(By.CSS_SELECTOR, "input[type='range']")
    range_value = driver.find_element(By.ID, "range")

    logger.info("Clicking on the slider to focus it.")
    slider.click()

    initial_value = range_value.text
    logger.info(f"Initial value of slider: {initial_value}")

    logger.info("Using the right arrow key to move the slider forward.")
    slider.send_keys(Keys.ARROW_RIGHT)

    WebDriverWait(driver, 3).until(
        lambda driver: range_value.text != initial_value
    )

    new_value = range_value.text
    logger.info(f"Slider value after moving forward: {new_value}")

    assert new_value != initial_value, f"Expected value to change, but got {new_value}"

    value_after_forward = new_value

    logger.info("Using the left arrow key to move the slider backward.")
    slider.send_keys(Keys.ARROW_LEFT)

    WebDriverWait(driver, 3).until(
        lambda driver: range_value.text != value_after_forward
    )
    new_value = range_value.text
    logger.info(f"Slider value after moving backward: {new_value}")

    assert new_value != value_after_forward, f"Expected value to change, but got {new_value}"

    logger.info("Horizontal Slider test passed successfully.")
