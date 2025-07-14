import pytest
from selene import browser



@pytest.fixture(autouse=True)
def browser_open():
    browser.config.window_width = 1280
    browser.config.window_height = 720
    yield
    browser.quit()