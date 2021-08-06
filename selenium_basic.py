import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

options = Options()
executable_path = os.getenv("EXECUTABLE_PATH")
assert (
    executable_path is not None
), "EXECUTABLE_PATH environment variable must be set"
logger.info(f"EXECUTABLE_PATH is {executable_path}")
options.binary_location = executable_path
options.add_argument("whitelisted-ips=''")
options.add_argument("disable-xss-auditor")
options.add_argument("disable-web-security")
options.add_argument("allow-running-insecure-content")
options.add_argument("no-sandbox")
options.add_argument("disable-setuid-sandbox")
options.add_argument("disable-popup-blocking")
options.add_argument("allow-elevated-browser")
options.add_argument("verbose")

def wait_for_spinner_visible(driver) -> None:
    """Wait for spinner to become visible.  This should take ~1 seconds."""
    spinner: tuple = (By.CSS_SELECTOR, "svg[class*=spin]")
    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located(spinner)
    )

driver = webdriver.Chrome(options=options)
wait_for_spinner_visible(driver)
driver.save_screenshot("screenshot.png")
driver.close()
