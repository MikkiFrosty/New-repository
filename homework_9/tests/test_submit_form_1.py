import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from homework_9.pages.registration_page import RegistrationPage

def test_fill_form():
    page = RegistrationPage()

    page.open_form()
    page.fill_firstname("София")
    page.fill_lastname("Кропотова")
    page.fill_email("sofia@example.com")
    page.fill_gender("Female")
    page.fill_phone("9220798421")
    page.fill_birthday(12, "June", 1997)
    page.fill_subject("Maths")
    page.fill_hobby("Sports")
    page.fill_file("test.png")
    page.fill_address("Нижний Новгород, ул. Королева, д. 4")
    page.fill_state_and_city("NCR", "Delhi")
    page.submit_form()

    page.check_result(
        "София Кропотова",
        "sofia@example.com",
        "Female",
        "9220798421",
        "12 June,1997",
        "Maths",
        "Sports",
        "test.png",
        "Нижний Новгород, ул. Королева, д. 4",
        "NCR Delhi"
    )