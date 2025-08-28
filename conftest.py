import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.options import Options
from utils import attach
from selene.support.shared import browser


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()
    global selenoid_login, selenoid_pass, selenoid_url
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    print("SELENOID_LOGIN =", selenoid_login)
    print("SELENOID_PASS =", selenoid_pass)
    print("SELENOID_URL =", selenoid_url)

@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()
    caps = {
        "browserName": "chrome",
        #"browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(caps)

    options.capabilities.update(caps)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",   #f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub" #"https://user1:1234@selenoid.autotests.cloud/wd/hub"
        options=options)

    browser.config.driver = driver  # Создаем объект Selene с WebDriver

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    driver.quit()