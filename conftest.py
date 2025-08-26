import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException
from dotenv import load_dotenv
import os as _os
from selene.support.shared import browser
from utils import attach

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope="function")
def remote_browser_setup():

    selenoid_login = _os.getenv("SELENOID_LOGIN")
    selenoid_pass = _os.getenv("SELENOID_PASS")
    selenoid_url = _os.getenv("SELENOID_URL")

    options = Options()
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True

        }
    }
    options.capabilities.update(selenoid_capabilities)

    selenoid_url = selenoid_url.replace('http://', '').replace('https://', '').rstrip('/')
    _os.environ['NO_PROXY'] = _os.environ.get('NO_PROXY', '') + ',selenoid.autotests.cloud'

    executor = f"http://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub"
    driver = webdriver.Remote(command_executor=executor, options=options)

    driver = webdriver.Remote(
        command_executor=executor,
        options=options
    )

    browser.config.driver = driver
    yield browser
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)

    try:
        browser.quit()
    except (InvalidSessionIdException, WebDriverException):
        pass