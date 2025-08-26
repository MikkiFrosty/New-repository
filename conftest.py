import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException
from dotenv import load_dotenv
import os as os
from selene.support.shared import browser
from utils import attach

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope="function")
def remote_browser_setup():

    selenoid_login = os.getenv("SELENOID_LOGIN", "user1")
    selenoid_pass = os.getenv("SELENOID_PASS", "1234")
    selenoid_url = os.getenv("SELENOID_URL", "selenoid.autotests.cloud")

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
    os.environ['NO_PROXY'] = os.environ.get('NO_PROXY', '') + ',selenoid.autotests.cloud'

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