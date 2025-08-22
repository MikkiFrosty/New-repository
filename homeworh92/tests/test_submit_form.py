from homework92.pages.registration_page import RegistrationPage
from homework92.models.user import User


def test_fill_form():
    sofi = User(
        first_name="София",
        last_name="Кропотова",
        email="sofia@example.com",
        gender="Female",
        phone="79220798421",
        day=12,
        month="June",
        year=1997,
        subject="Maths",
        hobby="Sports",
        file_name="test.png",
        address="Нижний Новгород, ул. Королева, д. 4",
        state="NCR",
        city="Delhi"
    )

    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(sofi)
    registration_page.should_have_registered(sofi)