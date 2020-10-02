import pytest
from selenium import webdriver

@pytest.fixture()
def setUp():
    driver=webdriver.Chrome("C:\\Users\\DELL\\Documents\\Downloads\\chromedriver.exe")
    return driver


