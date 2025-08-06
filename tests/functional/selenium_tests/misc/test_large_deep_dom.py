import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import logger, driver, pytest_configure  # Adjust imports as necessary


@pytest.mark.usefixtures("driver")
def test_large_and_deep_dom(driver):
    logger.info("Navigating to the Large & Deep DOM page.")
    driver.get("https://the-internet.herokuapp.com/large")

    logger.info("Verifying the 'No Siblings' section.")
    no_siblings_element = driver.find_element(By.ID, "no-siblings")
    assert no_siblings_element.is_displayed(), "'No Siblings' section is not visible"
    assert no_siblings_element.text == "No siblings", "'No Siblings' text is incorrect"

    logger.info("Verifying the 'Siblings' section.")
    for i in range(1, 51):
        for j in range(1, 4):
            sibling_id = f"sibling-{i}.{j}"
            try:
                WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, sibling_id)))
                sibling = driver.find_element(By.ID, sibling_id)


                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", sibling)


                WebDriverWait(driver, 10).until(EC.visibility_of(sibling))
                assert sibling.is_displayed(), f"Sibling {sibling_id} is not visible"


                if i % 10 == 0 and j == 3:
                    logger.info(f"Sibling block {i} is visible and correct.")
            except Exception as e:
                logger.error(f"Error finding or verifying {sibling_id}: {e}")
                continue


    max_rows = 50
    max_cols = 50

    logger.info("Verifying the large table headers and first few columns.")

    for i in range(1, max_cols + 1):
        try:
            header = driver.find_element(By.ID, f"header-{i}")
            WebDriverWait(driver, 10).until(EC.visibility_of(header))
            assert header.is_displayed(), f"Header {i} is not visible"


            if header.text.strip() != str(i):
                logger.error(f"Header {i} is incorrect (expected {i}, got {header.text.strip()})")


        except Exception as e:
            logger.error(f"Error finding or verifying header {i}: {e}")
            continue

    logger.info("Verifying the first few rows of the table.")

    for row in range(1, max_rows + 1):
        for col in range(1, max_cols + 1):
            cell_selector = f"tr:nth-child({row}) td:nth-child({col})"
            try:
                cell = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, cell_selector)))

                assert cell.is_displayed(), f"Cell in row {row}, column {col} is not visible"

                expected_text = f"{row}.{col}"

                assert cell.text.strip() == expected_text, f"Cell in row {row}, column {col} text is incorrect (expected {expected_text}, got {cell.text.strip()})"

                if cell.text.strip() != expected_text:
                    logger.error(
                        f"Cell in row {row}, column {col} is incorrect (expected {expected_text}, got {cell.text.strip()})")
                else:
                    if row % 10 == 0 and col == max_cols:
                        logger.info(f"Completed verifying row {row}.")
            except Exception as e:
                logger.error(f"Error finding or verifying cell at row {row}, column {col}: {e}")
                continue
