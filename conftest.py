import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service("C:\Users\pooja.db\Downloads\chromedriver-win32\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    driver.quit()