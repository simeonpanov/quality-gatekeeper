import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure

def test_hovers(driver):
    logger.info("Opening Hovers page.")
    driver.get("https://the-internet.herokuapp.com/hovers")

    user_avatars = driver.find_elements(By.CSS_SELECTOR, "div.figure img")

    for i, avatar in enumerate(user_avatars, 1):
        logger.info(f"Hovering over user {i} avatar.")
        ActionChains(driver).move_to_element(avatar).perform()

        figcaption = driver.find_element(By.XPATH, f"(//div[@class='figure'])[{i}]//div[@class='figcaption']")

        WebDriverWait(driver, 3).until(
            EC.visibility_of(figcaption)
        )

        name = figcaption.find_element(By.TAG_NAME, "h5").text
        assert name == f"name: user{i}", f"Expected name to be 'name: user{i}', but got {name}"

        profile_link = figcaption.find_element(By.TAG_NAME, "a").text
        assert profile_link == "View profile", f"Expected 'View profile' link text, but got {profile_link}"

    logger.info("Hovers test passed successfully.")
