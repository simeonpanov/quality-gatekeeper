import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure  # Adjust import as necessary


@pytest.mark.parametrize("username, password, expected_message, is_success", [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!", True),
    ("wronguser", "SuperSecretPassword!", "Your username is invalid!", False),
    ("tomsmith", "WrongPassword!", "Your password is invalid!", False),
    ("wronguser", "WrongPassword!", "Your username is invalid!", False),
])
def test_login(driver, username, password, expected_message, is_success):
    logger.info("Navigating to the Login page.")
    driver.get("https://the-internet.herokuapp.com/login")

    logger.info("Locating the username and password input fields.")
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    assert username_input.is_displayed(), "Username input field should be visible."
    assert password_input.is_displayed(), "Password input field should be visible."

    logger.info(f"Entering credentials - Username: {username}, Password: {'*' * len(password)}")
    username_input.send_keys(username)
    password_input.send_keys(password)

    logger.info("Clicking the 'Login' button.")
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()

    try:
        flash_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "flash"))
        ).text
        logger.info(f"Flash message displayed: {flash_message}")

        assert expected_message in flash_message, f"Expected '{expected_message}' in flash message."

        if is_success:
            assert "secure" in driver.current_url, "Did not navigate to the secure area after successful login."
            logger.info("Login successful. Navigated to secure area.")
        else:
            logger.info("Login failed as expected.")

    except Exception as e:
        logger.error(f"Expected flash message was not displayed: {e}")
        raise
