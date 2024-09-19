import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.base_page import BasePage


@pytest.fixture()
def browser():
    options = Options()
    prefs = {
        "download.default_directory": f"{os.getcwd()}\\files",
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    # options.add_argument("--headless")
    options.add_argument("--safebrowsing-disable-download-protection")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver


@pytest.fixture()
def page(browser):
    page = BasePage(browser=browser)
    page.open()  # Перейти на https://sbis.ru/
    return page
