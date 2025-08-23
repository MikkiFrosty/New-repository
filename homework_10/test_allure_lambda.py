import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s



def test_with_allure_steps():
    with allure.step('Открываем главную страницу'):
        browser.open("https://github.com")

    with allure.step('Ищем репозиторий eroshenkoam/allure-qaguru'):
        s(".search-input").click()
        s("#query-builder-test").should(be.visible).type("eroshenkoam/allure-qaguru")
        s("#query-builder-test").submit()

    with allure.step('Открываем eroshenkoam/allure-qaguru'):
        s(by.link_text("eroshenkoam/allure-qaguru")).click()

    with allure.step('Открываем issues'):
        s("#issues-tab").should(be.visible).click()
