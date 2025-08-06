from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import pytest
from config.config import logger, driver, pytest_configure  # Ensure proper imports for logger and driver

def test_challenging_dom(driver):
    logger.info("Navigating to the Challenging DOM page...")
    driver.get("https://the-internet.herokuapp.com/challenging_dom")

    def get_canvas_state():
        """Get the current state of the canvas for comparison."""
        return driver.execute_script("""
            var canvas = document.getElementById('canvas');
            var ctx = canvas.getContext('2d');
            return ctx.getImageData(0, 0, canvas.width, canvas.height).data.toString();
        """)

    canvas_locator = (By.ID, "canvas")

    # Capture the initial state of the canvas
    initial_canvas_state = get_canvas_state()
    logger.info("Initial canvas state captured.")

    buttons = {
        "bar": (By.XPATH, "//a[contains(@class, 'button') and not(contains(@class, 'alert')) and not(contains(@class, 'success'))]"),
        "qux": (By.XPATH, "//a[contains(@class, 'button alert')]"),
        "baz": (By.XPATH, "//a[contains(@class, 'button success')]")
    }

    for button_name, locator in buttons.items():
        button = driver.find_element(*locator)
        logger.info(f"Clicking the '{button_name}' button...")
        button.click()

        def canvas_state_has_changed():
            new_canvas_state = get_canvas_state()
            return new_canvas_state != initial_canvas_state

        WebDriverWait(driver, 10).until(
            lambda d: canvas_state_has_changed(),
            message=f"Canvas did not change after clicking the '{button_name}' button."
        )

        initial_canvas_state = get_canvas_state()
        logger.info(f"'{button_name}' button successfully changed the canvas.")

    for i in range(10):
        cell = driver.find_element(By.XPATH, f"//table/tbody/tr[{i + 1}]/td[1]")
        expected_text = f"Iuvaret{i}"
        assert cell.text == expected_text, f"Expected '{expected_text}', but got '{cell.text}'."
        logger.info(f"Row {i} content verified: {cell.text}")

        edit_button = driver.find_element(By.XPATH, f"//table/tbody/tr[{i + 1}]//a[text()='edit']")
        delete_button_locator = (By.XPATH, f"//table/tbody/tr[{i + 1}]//a[text()='delete']")

        logger.info(f"Clicking 'edit' button in row {i}...")
        edit_button.click()
        WebDriverWait(driver, 10).until(EC.url_contains("#edit"))
        assert '#edit' in driver.current_url, f"URL fragment '#edit' not found after clicking 'edit' button in row {i}."
        logger.info(f"'edit' button in row {i} updated URL correctly to: {driver.current_url}")

        driver.get("https://the-internet.herokuapp.com/challenging_dom")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table")))

        delete_button = driver.find_element(*delete_button_locator)

        logger.info(f"Clicking 'delete' button in row {i}...")
        delete_button.click()
        logger.info(f"'delete' button in row {i} clicked successfully.")

    logger.info("All table content verified and URL fragment checks completed.")

