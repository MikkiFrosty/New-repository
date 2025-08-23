import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")

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



