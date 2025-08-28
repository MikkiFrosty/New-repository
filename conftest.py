import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException
from selene import browser
from utils import attach

load_dotenv()  # .env

@pytest.fixture(scope='function', autouse=True)
def remote_browser_setup():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selene.support.shared import browser
    from selenium.common.exceptions import InvalidSessionIdException, WebDriverException
    import os

    login = os.getenv("SELENOID_LOGIN")
    password = os.getenv("SELENOID_PASS")
    host = os.getenv("SELENOID_URL", "").replace('http://','').replace('https://','').rstrip('/')

    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {"enableVNC": True, "enableVideo": True})
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{host}/wd/hub",
        options=options
    )
    browser.config.driver = driver

    yield

    try:
        browser.quit()
    except (InvalidSessionIdException, WebDriverException):
        pass