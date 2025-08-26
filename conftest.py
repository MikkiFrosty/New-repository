import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException

from dotenv import load_dotenv
import os
from selene.support.shared import browser
from utils import attach

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope="function")
def remote_browser_setup():
    from dotenv import load_dotenv
    import os
    load_dotenv()

    login = os.getenv("SELENOID_LOGIN")
    password = os.getenv("SELENOID_PASS")
    host = os.getenv("SELENOID_URL")  # только домен

    assert all([login, password, host]), f"ENV missing: login={bool(login)}, pass={bool(password)}, url={bool(host)}"

    # чистим host и на всякий случай выключаем прокси для selenoid
    host = host.replace('http://', '').replace('https://', '').rstrip('/')
    os.environ['NO_PROXY'] = os.environ.get('NO_PROXY', '') + ',selenoid.autotests.cloud'

    # настраиваем options ДО создания драйвера
    options = Options()
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)

    executor = f"https://{login}:{password}@{host}/wd/hub"
    driver = webdriver.Remote(command_executor=executor, options=options)

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