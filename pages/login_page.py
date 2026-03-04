from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    username = (By.ID, "username")
    password = (By.ID, "password")
    submit = (By.ID, "submit")
    logout = (By.XPATH, "//a[normalize-space()='Log out']")
    error_message = (By.ID, "error")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.submit)).click()

    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.logout)).click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_message)).text