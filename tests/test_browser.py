import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.main import LOGIN_URL, USERNAME, PASSWORD


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_and_product_page(browser):
    browser.get(LOGIN_URL)

    username_input = browser.find_element(By.ID, "user-name")
    username_input.send_keys(USERNAME)

    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys(PASSWORD)

    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()

    time.sleep(2)
    #добираемся до перечня товаров, если есть - вошли
    products_table = browser.find_elements(By.CLASS_NAME, "inventory_list")

    assert len(products_table) > 0, "Таблица с товарами не найдена на странице."
