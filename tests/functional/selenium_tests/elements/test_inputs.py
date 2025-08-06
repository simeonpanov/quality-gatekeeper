import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config.config import logger, driver, pytest_configure


def test_input_number_field(driver):
    logger.info("Opening Inputs page.")
    driver.get("https://the-internet.herokuapp.com/inputs")

    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

    input_value = 42  # Example number to enter
    logger.info(f"Entering the number {input_value} into the input field.")
    input_field.clear()  # Clear any existing value in the input field
    input_field.send_keys(input_value)  # Enter the number

    entered_value = input_field.get_attribute("value")
    logger.info(f"Entered value is {entered_value}.")

    assert entered_value == str(input_value), f"Expected value '{input_value}', but got '{entered_value}'."

    logger.info("Input number test passed successfully.")
