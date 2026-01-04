
import pytest
from selenium import webdriver

from data.urls import BasicUrls


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BasicUrls.HOME)
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    """Фикстура для создания HomePage объекта"""
    from pages.home_page import HomePage
    page = HomePage(driver)
    page.open()
    return page