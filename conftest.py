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
    """
    Автоматически поднимает браузер перед каждым тестом
    и прикладывает аттачи после.
    """

    # базовые настройки Selene
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1200
    browser.config.window_height = 900
    browser.config.timeout = 4.0

    # если переменные заданы — едем в Selenoid, иначе можно запустить локально (по желанию)
    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASS')
    host = os.getenv('SELENOID_URL')  # только домен, без схемы и /wd/hub

    if login and password and host:
        host = host.replace('http://', '').replace('https://', '').rstrip('/')
        os.environ['NO_PROXY'] = os.environ.get('NO_PROXY', '') + ',selenoid.autotests.cloud'

        options = Options()
        options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
        options.set_capability('browserName', 'chrome')
        options.set_capability('browserVersion', '128.0')
        options.set_capability('selenoid:options', {'enableVNC': True, 'enableVideo': True})

        executor = f'https://{login}:{password}@{host}/wd/hub'
        browser.config.driver = webdriver.Remote(command_executor=executor, options=options)
    else:
        # если хочешь падать без переменных — раскомментируй строку ниже
        # raise AssertionError('No Selenoid creds/host in .env')
        pass

    yield

    # --- аттачи
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)  # для Selenoid

    try:
        browser.quit()
    except (InvalidSessionIdException, WebDriverException):
        pass