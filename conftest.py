import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
    executable_path="C:\\WebDrivers\\chromedriver\\chromedriver.exe",
    options=options
    )

    yield driver

    driver.quit()