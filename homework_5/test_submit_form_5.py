import pytest
import os
from selene import browser, have, be

def test_submit_form():
    browser.open('/automation-practice-form')
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test.png'))


    browser.element('#firstName').type('София')
    browser.element('#lastName').type('Кропотова')
    browser.element('#userEmail').type('sofia@example.com')
    browser.element('#gender-radio-2').double_click()
    browser.element('#userNumber').type('79999999999')


    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('June')
    browser.element('.react-datepicker__year-select').send_keys('1997')
    browser.element('.react-datepicker__day--012').click()


    browser.element('#subjectsInput').should(be.visible).type('Maths').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()


    browser.element('#uploadPicture').send_keys(file_path)


    browser.element('#currentAddress').type('Нижний Новгород, ул. Королева, д. 4')
    browser.element('#state').click().element('#react-select-3-option-0').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()


    browser.element('#submit').press_enter()


    browser.element('.modal-content').should(have.text('София Кропотова'))
    browser.element('.modal-content').should(have.text('sofia@example.com'))
    browser.element('.modal-content').should(have.text('Female'))
    browser.element('.modal-content').should(have.text('7999999999'))
    browser.element('.modal-content').should(have.text('12 June,1997'))
    browser.element('.modal-content').should(have.text('Maths'))
    browser.element('.modal-content').should(have.text('Sports'))
    browser.element('.modal-content').should(have.text('test.png'))
    browser.element('.modal-content').should(have.text('Нижний Новгород, ул. Королева, д. 4'))
    browser.element('.modal-content').should(have.text('NCR Delhi'))
