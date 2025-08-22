import pytest
import os
from selene import browser, have, be


class RegistrationPage:
    def open_form(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def fill_firstname(self, firstname: str):
        browser.element('#firstName').type(firstname)
        return self

    def fill_lastname(self, lastname: str):
        browser.element('#lastName').type(lastname)
        return self

    def fill_email(self, email: str):
        browser.element('#userEmail').type(email)
        return self

    def fill_gender(self, gender: str):
        browser.element('#gender-radio-2').double_click()
        return self

    def fill_phone(self, phone: str):
        browser.element('#userNumber').type(phone)
        return self

    def fill_birthday(self, day: int, month: str, year: int):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(str(year))
        browser.element(f'.react-datepicker__day--0{day:02d}').click()
        return self

    def fill_subject(self, subject: str):
        browser.element('#subjectsInput').should(be.visible).type(subject).press_enter()
        return self

    def fill_hobby(self, hobby: str):
        browser.element('[for=hobbies-checkbox-1]').click()
        return self

    def fill_file(self, file_name: str):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "resources", file_name))
        browser.element('#uploadPicture').send_keys(file_path)
        return self

    def fill_address(self, address: str):
        browser.element('#currentAddress').type(address)
        return self

    def fill_state_and_city(self, state: str, city: str):
        browser.element('#state').click().element('#react-select-3-option-0').click()
        browser.element('#city').click().element('#react-select-4-option-0').click()
        return self

    def submit_form(self):
        browser.element('#submit').press_enter()
        return self

    def check_result(self, *expected_texts: str):
        modal = browser.element('.modal-content').should(be.visible)
        for text in expected_texts:
            modal.should(have.text(text))
        return self