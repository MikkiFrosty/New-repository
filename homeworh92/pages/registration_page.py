import os
from selene import browser, have, be
from homeworh92.models.user import User
from pathlib import Path

class RegistrationPage:

    def open_form(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def register(self, user: User):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources', user.file_name))

        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.element(f'//label[text()="{user.gender}"]').click()
        browser.element('#userNumber').type(user.phone)

        # birthday
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(user.month)
        browser.element('.react-datepicker__year-select').send_keys(str(user.year))
        browser.element(f'.react-datepicker__day--0{user.day:02}').click()

        browser.element('#subjectsInput').should(be.visible).type(user.subject).press_enter()
        browser.element(f'//label[text()="{user.hobby}"]').click()
        browser.element('#uploadPicture').send_keys(file_path)
        browser.element('#currentAddress').type(user.address)
        browser.element('#state').click().element(f'//div[text()="{user.state}"]').click()
        browser.element('#city').click().element(f'//div[text()="{user.city}"]').click()

        browser.element('#submit').press_enter()
        return self

    def should_have_registered(self, user: User):
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