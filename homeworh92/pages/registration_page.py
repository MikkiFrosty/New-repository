import os
import allure
from selene import have, be, by
from selene.support.shared import browser
from homeworh92.models.user import User


class RegistrationPage:
    def open_form(self):
        with allure.step("Переход на страницу"):
            browser.open('https://demoqa.com/automation-practice-form')
            browser.driver.set_window_size(1920, 1080)
            browser.driver.execute_script("document.querySelector('#fixedban')?.remove();")
            browser.driver.execute_script("document.querySelector('footer')?.remove();")
        return self

    def register(self, user: User):
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'resources', user.file_name)
        )

        with allure.step("Заполнение имени"):
            browser.element('#firstName').type(user.first_name)
        with allure.step("Заполнение фамилии"):
            browser.element('#lastName').type(user.last_name)
        with allure.step("Заполнение емейла"):
            browser.element('#userEmail').type(user.email)
        with allure.step("Выбор пола"):
            browser.element(f'//label[text()="{user.gender}"]').click()
        with allure.step("Заполнение номера телефона"):
            browser.element('#userNumber').type(user.phone)

        with allure.step("Заполнение даты рождения"):
            browser.element('#dateOfBirthInput').click()
            browser.element('.react-datepicker__month-select').send_keys(user.month)
            browser.element('.react-datepicker__year-select').send_keys(str(user.year))
            browser.element(f'.react-datepicker__day--0{user.day:02}').click()

        with allure.step("Выбор предмета"):
            browser.element('#subjectsInput').should(be.visible).type(user.subject).press_enter()

        with allure.step("Выбор хобби"):
            browser.element('label[for ="hobbies-checkbox-1"]').click()

        with allure.step("Загрузка изображения"):
            browser.element('#uploadPicture').send_keys(file_path)

        with allure.step("Выбор адреса"):
            browser.element('#currentAddress').type(user.address)
            browser.element('#state').click()
            browser.element(f'//div[text()="{user.state}"]').click()
            browser.element('#city').click()
            browser.element(f'//div[text()="{user.city}"]').click()

        with allure.step("Отправка формы"):
            browser.element('#submit').press_enter()

        return self

    def should_have_registered(self, user: User):
        with allure.step("Проверка формы"):
            modal = browser.element('.modal-content')
            modal.should(have.text(f'{user.first_name} {user.last_name}'))
            modal.should(have.text(user.email))
            modal.should(have.text(user.gender))
            modal.should(have.text(user.phone))
            modal.should(have.text(f'{user.day} {user.month},{user.year}'))
            modal.should(have.text(user.subject))
            modal.should(have.text(user.hobby))
            modal.should(have.text(user.file_name))
            modal.should(have.text(user.address))
            modal.should(have.text(f'{user.state} {user.city}'))