from pages.login_page import LoginPage
from config.config import BASE_URL

def test_invalid_login(browser):

    browser.get(BASE_URL)

    login = LoginPage(browser)

    login.enter_username("student_1234")
    login.enter_password("Password123")
    login.click_submit()

    error = login.get_error_message()

    assert error == "Your username is invalid!"