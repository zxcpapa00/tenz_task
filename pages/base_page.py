import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def open(self):
        self.browser.get("https://sbis.ru/")

    def wait_element_to_be_clickable(self, args):
        wait = WebDriverWait(self.browser, 10)
        element = wait.until(
            ec.element_to_be_clickable(args))
        return element

    def click_button_contacts(self):
        element = self.wait_element_to_be_clickable(
            (By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[3]/a'))
        element.click()

    def click_button_about(self):
        element = self.wait_element_to_be_clickable(
            (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a'))
        self.browser.execute_script("arguments[0].click();", element)

    def click_logo_tenzor(self):
        element = self.wait_element_to_be_clickable(
            (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a'))
        element.click()
        self.switch_window()

    def get_current_url(self):
        return self.browser.current_url

    def switch_window(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)

    def get_size_img(self):
        block = self.find((By.XPATH, '//*[@id="container"]/div[1]/div/div[4]'))
        imgs = block.find_elements(By.CLASS_NAME, 'tensor_ru-About__block3-image')
        img_sizes = [img.size for img in imgs]
        return img_sizes
