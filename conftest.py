# import pytest
# from selenium import webdriver

# @pytest.fixture
# def browser():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()

import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()