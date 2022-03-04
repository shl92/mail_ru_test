import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    """Fixture function to launch browser and close browser at the end of the test."""
    print("\nStart Chrome browser")
    option = Options()
    option.add_argument("--headless")
    browser = webdriver.Chrome(options=option)
    browser.set_window_size(1920, 1080)
    yield browser
    print("\nClose browser.")
    browser.quit()
