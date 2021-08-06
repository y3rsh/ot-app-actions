import os
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

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


driver = webdriver.Chrome(options=options)
driver.get("https://opentrons.com")
assert "Opentrons" in driver.title
assert "$5,000" in driver.page_source
driver.save_screenshot("screenshot.png")
driver.close()
