import pytest
from selene import browser

@pytest.fixture(autouse=True)
def setup_browser():
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()

