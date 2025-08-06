import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure  # Adjust import as necessary


@pytest.mark.usefixtures("driver")
def test_key_presses(driver):
    logger.info("Navigating to the Key Presses page.")
    driver.get("https://the-internet.herokuapp.com/key_presses")

    logger.info("Locating the input field.")
    input_field = driver.find_element(By.ID, "target")

    key_press_scenarios = [
        ('a', "A"),
        ('b', "B"),
        (Keys.SPACE, "SPACE"),
        (Keys.ESCAPE, "ESCAPE"),
        (Keys.TAB, "TAB"),
        (Keys.SHIFT, "SHIFT"),
        (Keys.CONTROL, "CONTROL"),
        (Keys.ARROW_UP, "UP"),
        (Keys.ARROW_DOWN, "DOWN"),
        (Keys.NUMPAD0, "NUMPAD0"),
        (Keys.NUMPAD9, "NUMPAD9"),
        (Keys.F1, "F1"),
        (Keys.F12, "F12")
    ]

    for key, expected_output in key_press_scenarios:
        logger.info(f"Pressing key: {expected_output}")

        input_field.clear()

        input_field.send_keys(key)

        try:
            result_text = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "result"))
            ).text

            logger.info(f"Result text after pressing '{expected_output}': {result_text}")

            assert result_text == f"You entered: {expected_output}", f"Unexpected result for key '{expected_output}'"

        except Exception as e:
            logger.error(f"Error occurred when pressing '{expected_output}': {str(e)}")
            raise
