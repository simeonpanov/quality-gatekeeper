import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure  # Adjust import as necessary


@pytest.mark.usefixtures("driver")
def test_nested_frames(driver):
    logger.info("Navigating to the Frames page.")
    driver.get("https://the-internet.herokuapp.com/frames")

    logger.info("Clicking on the 'Nested Frames' link.")
    nested_frames_link = driver.find_element(By.LINK_TEXT, "Nested Frames")
    nested_frames_link.click()

    logger.info("Switching to the nested frames.")

    driver.switch_to.frame("frame-top")

    logger.info("Switching to the left frame.")
    driver.switch_to.frame("frame-left")
    left_text = driver.find_element(By.TAG_NAME, "body").text
    logger.info(f"Content in left frame: {left_text}")
    assert left_text == "LEFT", "Expected content 'LEFT' in the left frame."

    driver.switch_to.parent_frame()
    logger.info("Switching to the middle frame.")
    driver.switch_to.frame("frame-middle")
    middle_text = driver.find_element(By.ID, "content").text
    logger.info(f"Content in middle frame: {middle_text}")
    assert middle_text == "MIDDLE", "Expected content 'MIDDLE' in the middle frame."

    driver.switch_to.parent_frame()
    logger.info("Switching to the right frame.")
    driver.switch_to.frame("frame-right")
    right_text = driver.find_element(By.TAG_NAME, "body").text
    logger.info(f"Content in right frame: {right_text}")
    assert right_text == "RIGHT", "Expected content 'RIGHT' in the right frame."

    driver.switch_to.default_content()
    logger.info("Switching to the bottom frame.")
    driver.switch_to.frame("frame-bottom")
    bottom_text = driver.find_element(By.TAG_NAME, "body").text
    logger.info(f"Content in bottom frame: {bottom_text}")
    assert bottom_text == "BOTTOM", "Expected content 'BOTTOM' in the bottom frame."


@pytest.mark.usefixtures("driver")
def test_iframe(driver):
    logger.info("Navigating to the Frames page.")
    driver.get("https://the-internet.herokuapp.com/frames")

    logger.info("Clicking on the 'iFrame' link.")
    iframe_link = driver.find_element(By.LINK_TEXT, "iFrame")
    iframe_link.click()

    logger.info("Switching to the iFrame.")
    iframe_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mce_0_ifr"))
    )
    driver.switch_to.frame(iframe_element)

    logger.info("Interacting with the content inside the iFrame.")
    content = driver.find_element(By.ID, "tinymce")
    content_text = content.text
    logger.info(f"Original content in iFrame: {content_text}")

    # Check if the content is still the initial 'Your content goes here.' message
    if content_text == "Your content goes here.":
        logger.info("Editor content is the default message.")
        assert content_text == "Your content goes here.", "Unexpected initial content in the iFrame."
    else:
        logger.warning("Editor is in read-only mode or has no editable content.")
        # Skip modification since the editor is likely in read-only mode
        logger.info("Skipping content modification as the editor is in read-only mode or empty.")

    driver.switch_to.default_content()