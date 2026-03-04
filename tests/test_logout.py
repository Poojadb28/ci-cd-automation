from pages.login_page import LoginPage
from config.config import BASE_URL

def test_logout(browser):

    browser.get(BASE_URL)

    login = LoginPage(browser)

    login.enter_username("student")
    login.enter_password("Password123")
    login.click_submit()

    login.click_logout()

    assert browser.current_url == BASE_URL