from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_logout(browser):
    wait=WebDriverWait(browser,20)
    browser.get("https://practicetestautomation.com/practice-test-login/")

    # Enter username 
    wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='username']"))).send_keys("student")

    # Enter Password
    wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='password']"))).send_keys("Password123")

    # Click on submit button
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='submit']"))).click()

    # Click on logout button
    wait.until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Log out']"))).click()

    # assertion for change in url
    assert browser.current_url == "https://practicetestautomation.com/practice-test-login/"


