from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_invalid_login(browser):
    wait=WebDriverWait(browser,20)
    browser.get("https://practicetestautomation.com/practice-test-login/")

    # Enter incorrectusername 
    wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='username']"))).send_keys("student_1234")

    # Enter Password
    wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='password']"))).send_keys("Password123")

    # Click on submit button
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='submit']"))).click()

    # assertion for error message
    error_message = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='error']"))).text
    assert error_message == "Your username is invalid!"
