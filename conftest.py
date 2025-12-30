
import pytest
from selenium import webdriver

from data.urls import BasicUrls


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BasicUrls.HOME)
    yield driver
    driver.quit()