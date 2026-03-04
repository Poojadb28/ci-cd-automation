from pages.login_page import LoginPage
from config.config import BASE_URL


def test_login(browser):

    browser.get(BASE_URL)

    login = LoginPage(browser)

    login.enter_username("student")
    login.enter_password("Password123")
    login.click_submit()

    assert browser.current_url == "https://practicetestautomation.com/logged-in-successfully/"