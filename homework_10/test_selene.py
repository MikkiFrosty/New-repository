from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s



def test_selene():
    browser.open("https://github.com")
    s(".search-input").click()
    s("#query-builder-test").should(be.visible).type("eroshenkoam/allure-qaguru")
    s("#query-builder-test").submit()
    s(by.link_text("eroshenkoam/allure-qaguru")).click()
    s("#issues-tab").should(be.visible).click()



